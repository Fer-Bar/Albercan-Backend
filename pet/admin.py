from django.contrib import admin

from pet.models import Breed, Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    search_fields = ["name", "owner"]
    list_display = ("name", "breed", "age", "owner")
    readonly_fields = ("age", )


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    search_fields = ["name"]


class PetInline(admin.TabularInline):
    model = Pet
    extra = 0
