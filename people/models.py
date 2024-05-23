from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Person(models.Model):
    GENDER_CHOICES = (
        ("F", _("Female")),
        ("M", _("Male")),
    )
    DOCUMENT_TYPE_CHOICES = (
        ("DNI", _("Identity Card")),
        ("Passport", _("Passport"))
    )
    EDUCATIONAL_LEVEL_CHOICES = (
        ("Primary", _("Primary school")),
        ("Secondary", _("Secondary school")),
        ("Tertiary", _("Tertiary")),
        ("University", _("University")),
        ("Postgraduate", _("Postgraduate")),
        ("TBC", _("To be confirmed")),
    )
    MARITAL_STATUS_CHOICES = (
        ("Single", _("Single")),
        ("Married", _("Married")),
        ("Separated", _("Separated")),
        ("Divorced", _("Divorced")),
        ("Widowed", _("Widowed")),
        ("Stable Bond", _("Stable Bond")),
        ("Other", _("Other")),
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="person",
        verbose_name=_("user"),
        null=True,
    )
    first_name = models.CharField(
        max_length=30,
        verbose_name=_("first name"),
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name=_("last name"),
    )
    birthday = models.DateField(null=True, blank=True, verbose_name=_("birthday"))
    nationality = models.ForeignKey(
        "structure.Country",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("nationality"),
    )
    document_type = models.CharField(
        max_length=30,
        verbose_name=_("document type"),
        null=True,
        blank=True,
        default="DNI",
        choices=DOCUMENT_TYPE_CHOICES,
    )
    document_id = models.CharField(
        max_length=100,
        verbose_name=_("document id"),
        null=True,
        blank=True,
    )
    educational_level = models.CharField(
        choices=EDUCATIONAL_LEVEL_CHOICES,
        max_length=100,
        verbose_name=_("educational level"),
        null=True,
        blank=True,
    )
    personal_email = models.EmailField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("personal email"),
        unique=True,
    )
    phone_number = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("phone number"),
        help_text=f"+591 70101010 {_('(spaces are optional)')}"
    )
    secondary_phone_number = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("secondary phone number"),
        help_text=f"+591 70101010 {_('(spaces are optional)')}"
    )
    address = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("address"),
    )
    city = models.ForeignKey(
        "structure.City",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name=_("city"),
    )
    neighborhood = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("neighborhood"),
    )

    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True,
        verbose_name=_("gender"),
    )
    occupation = models.ForeignKey(
        "Occupation",
        related_name="person",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name=_("occupation"),
    )
    marital_status = models.CharField(
        choices=MARITAL_STATUS_CHOICES,
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("marital status"),
    )
    picture = models.ImageField(
        upload_to="people_images/",
        null=True,
        blank=True,
        verbose_name=_("picture"),
        help_text=_("Max size allowed: 20Mbs"),
    )

    @property
    def picture_url(self):
        """
        Return self.picture.url if self.picture is not None,
        'url' exist and has a value, else, return None.
        """
        if self.picture and hasattr(self.picture, "url"):
            return self.picture.url

    def create_user(self):
        if self.user_id is not None:
            return
        self.user, _ = User.objects.get_or_create(
            username=self.personal_email,
            defaults={
                "email": self.personal_email,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "is_staff": True
            }
        )

    def deactivate_user(self):
        if not self.user_id:
            return
        self.user.is_staff = False
        self.user.is_active = False
        self.user.save()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name_plural = _("People")
        constraints = [
            models.UniqueConstraint(
                name="%(app_label)s_%(class)s_unique_nationality_document_type_and_id",
                fields=("nationality", "document_type", "document_id"),
            ),
        ]


class ContactWay(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = _("contact way")
        verbose_name_plural = _("contact ways")


class Occupation(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = _("occupation")
        verbose_name_plural = _("occupations")
