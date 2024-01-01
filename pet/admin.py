from django.contrib import admin
from pet.models import Pet, Race


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    search_fields = ["name"]


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    search_fields = ["name"]


class PetInline(admin.TabularInline):
    model = Pet
    extra = 0

