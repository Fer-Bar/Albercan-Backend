from django.contrib import admin

from structure.models import City, Country, Departament


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    search_fields = ("name", "department__name", "department__country__name")
    list_display = ("name", "department", "country")
    autocomplete_fields = ("department", )


@admin.register(Departament)
class DepartamentAdmin(admin.ModelAdmin):
    search_fields = ("name", "country__name")
    list_display = ("name", "country")
    autocomplete_fields = ("country", )


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    search_fields = ("name", )
