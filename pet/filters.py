from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class HasOwnerFilter(admin.SimpleListFilter):
    title = _('Has owner')
    parameter_name = 'has_owner'

    def lookups(self, request, model_admin):
        return (
            ('yes', _('Yes')),
            ('no', _('No')),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'yes':
            return queryset.exclude(owner__isnull=True)
        elif value == 'no':
            return queryset.filter(owner__isnull=True)
