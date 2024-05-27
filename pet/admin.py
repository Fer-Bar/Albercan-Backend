from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from pet.filters import HasOwnerFilter
from pet.models import Breed, Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    search_fields = ["name", "owner"]
    list_display = ("name", "breed", "gender", "age", "owner", "has_owner", "is_neutered")
    readonly_fields = ("age", "picture_display",)
    list_filter = (HasOwnerFilter,)

    def picture_display(self, obj=None):
        return mark_safe(
            f'<img style="object-fit: cover;" src="{obj.picture_url}" height=250 width=100%>'
        )

    picture_display.short_description = _("Profile Picture")

    def get_fieldsets(self, request, obj=None):
        if obj is None or not obj.picture_url:
            picture_fields = [
                ("picture",),
            ]
        else:
            picture_fields = [
                ("picture_display", "picture"),
            ]
        return (
            (
                None, {
                    "fields": picture_fields + [("name", "breed", "gender", "birthday", "age"), ]
                }
            ),
        )


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    search_fields = ["name"]


class PetInline(admin.TabularInline):
    model = Pet
    fields = ("name", "breed", "gender")
    extra = 0
