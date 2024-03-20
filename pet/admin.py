from django.contrib import admin

from pet.filters import HasOwnerFilter
from pet.models import Breed, Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    search_fields = ["name", "owner"]
    list_display = ("name", "breed", "gender", "age", "owner", "has_owner", "is_neutered")
    readonly_fields = ("age", )
    list_filter = (HasOwnerFilter,)


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    search_fields = ["name"]


class PetInline(admin.TabularInline):
    model = Pet
    extra = 0
