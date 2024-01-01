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
        "user",
        "occupation",
        "city",
        "nationality",
    ]

    def picture_display(self, obj=None):
        return mark_safe(f'<img src="{obj.picture.url}" height=250>')

    picture_display.short_description = _("See picture")

    def get_readonly_fields(self, request, obj=None):
        return ["picture_display",]

    def get_fieldsets(self, request, obj=None):
        if obj is None or not obj.picture:
            main_fields = [
                ("picture",),
                ("first_name", "last_name", "gender"),
            ]
        else:
            main_fields = [
                (
                    "picture_display",
                    "picture",
                    "first_name",
                    "last_name",
                    "gender",
                ),
            ]

        return (
            (
                _("Main Data"),
                {
                    "fields": main_fields
                    + [
                        ("city",),
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
                        ("nationality", ),
                        ("address", ),
                        ("neighborhood", ),
                        ("occupation", ),
                    ]
                },
            ),
        )


@admin.register(Person)
class PersonAdmin(BasePersonAdmin):

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj=obj)
        return fieldsets

    def has_delete_permission(
        self, request, obj=None
    ):  # This allows to delete only if you're a superuser
        return request.user.is_superuser and request.user.is_active

    inlines = [PetInline,]
