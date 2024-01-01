from django.contrib import admin

from pet.models import Breed, Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    search_fields = ["name"]


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    search_fields = ["name"]


class PetInline(admin.TabularInline):
    model = Pet
    extra = 0
