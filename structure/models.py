from django.db import models
from django.utils.translation import gettext_lazy as _


class Country(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name=_("name"))

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name = _("country")
        verbose_name_plural = _("countries")


class Departament(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("name"))
    country = models.ForeignKey("Country", on_delete=models.CASCADE, verbose_name=_("country"))

    def __str__(self) -> str:
        return f"{self.name}, {self.country}"

    class Meta:
        ordering = ("name",)
        verbose_name = _("department")
        verbose_name_plural = _("departments")
        unique_together = ("name", "country")


class City(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("name"))
    department = models.ForeignKey(
        "Departament",
        on_delete=models.CASCADE,
        verbose_name=_("department")
    )

    def __str__(self) -> str:
        return self.name

    def country(self) -> Country:
        return self.department.country

    class Meta:
        ordering = ("name",)
        verbose_name = _("city")
        verbose_name_plural = _("cities")
        unique_together = ("name", "department")
