from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.datetools import calculate_pet_age, first_of_month


class Pet(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False, verbose_name=_("name"))
    owner = models.ForeignKey("people.Person", on_delete=models.PROTECT)
    birthday = models.DateField(null=True, blank=True, verbose_name=_("birth_date"))
    breed = models.ForeignKey(
        "Breed",
        related_name="pet",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name=_("breed")
    )

    @property
    def age(self):
        today = first_of_month(is_datetime=True)
        age = calculate_pet_age(self.birthday, today)
        return _(f"{age.years} years, {age.months} months.")

    def __str__(self):
        return self.name


class Breed(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)
