from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from people.models import ContactWay, Occupation, Person
from pet.admin import PetInline


@admin.register(Occupation)
class OccupationAdmin(admin.ModelAdmin):
    search_fields = ["name"]


@admin.register(ContactWay)
class ContactWayAdmin(admin.ModelAdmin):
    search_fields = ["name"]


class BasePersonAdmin(ModelAdmin):
    list_display = ["last_name", "first_name", "nationality", "occupation"]
    search_fields = [
        "first_name",
        "last_name",
        "user__email",
    ]
    autocomplete_fields = [
        "occupation",
        "city",
        "nationality",
    ]

    def picture_display(self, obj=None):
        return mark_safe(
            f'<img style="object-fit: cover;" src="{obj.picture_url}" height=250 width=100%>'
        )

    picture_display.short_description = _("Profile Picture")

    readonly_fields = ("picture_display",)

    def get_fieldsets(self, request, obj=None):
        if obj is None or not obj.picture:
            main_fields = [
                ("picture",),
            ]
        else:
            main_fields = [
                (
                    "picture_display",
                    "picture",
                ),
            ]

        return (
            (
                _("Main Data"),
                {
                    "fields": main_fields
                    + [
                        ("first_name", "last_name", "gender", "city"),
                        ("personal_email", "birthday"),
                    ]
                },
            ),
            (
                _("Other Data"),
                {
                    "fields": [
                        ("document_type", "document_id"),
                        ("marital_status",),
                        ("phone_number", "secondary_phone_number"),
                        ("nationality",),
                        ("address",),
                        ("neighborhood",),
                        ("occupation",),
                    ]
                },
            ),
        )


@admin.register(Person)
class PersonAdmin(BasePersonAdmin):
    list_display = ["first_name", "last_name", "list_pets",]
    inlines = [
        PetInline,
    ]

    def has_delete_permission(
        self, request, obj=None
    ):  # This allows to delete only if you're a superuser
        return request.user.is_superuser and request.user.is_active

    def list_pets(self, obj):
        return ", ".join([str(pet) for pet in obj.pets.all()])

    list_pets.short_description = _("My Pets")
