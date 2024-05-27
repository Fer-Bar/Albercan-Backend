from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.datetools import calculate_pet_age, first_of_month


class Pet(models.Model):
    GENDER_CHOICES = (
        ("F", _("Female")),
        ("M", _("Male")),
    )
    name = models.CharField(
        max_length=40, blank=False, null=False, verbose_name=_("name")
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True,
        verbose_name=_("gender"),
    )
    owner = models.ForeignKey(
        "people.Person",
        on_delete=models.SET_NULL,
        related_name="pets",
        null=True,
        blank=True,
        verbose_name=_("owner"),
    )
    birthday = models.DateField(null=True, blank=True, verbose_name=_("birth_date"))
    breed = models.ForeignKey(
        "Breed",
        related_name="pets",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name=_("breed"),
    )
    is_neutered = models.BooleanField(default=False, verbose_name=_("is_neutered"))
    picture = models.ImageField(
        upload_to="pet/",
        null=True,
        blank=True,
        verbose_name=_("picture"),
        help_text=_("Max size allowed: 20Mbs"),
    )

    @property
    def age(self):
        if self.birthday:
            today = first_of_month(is_datetime=True)
            age = calculate_pet_age(self.birthday, today)
            return _(f"{age.years} years, {age.months} months.")

    @property
    def picture_url(self):
        """
        Return self.picture.url if self.picture is not None,
        'url' exist and has a value, else, return None.
        """
        if self.picture and hasattr(self.picture, "url"):
            return self.picture.url

    @property
    def has_owner(self):
        return self.owner is not None

    def __str__(self):
        return self.name


class Breed(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)

    def __str__(self):
        return self.name
