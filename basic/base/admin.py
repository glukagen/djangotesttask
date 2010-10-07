from base.models import Location, Person
from django.contrib import admin


class LocationAdmin(admin.ModelAdmin):
    def make_priority_0(self, request, queryset):
        rows_updated = queryset.update(priority=0)
        self.message_user(request,
            "%s location priorities successfully marked as 0." % rows_updated)
    make_priority_0.short_description = "Mark selected location priority as 0"

    def make_priority_1(self, request, queryset):
        rows_updated = queryset.update(priority=1)
        self.message_user(request,
            "%s location priorities successfully marked as 1." % rows_updated)
    make_priority_1.short_description = "Mark selected location priority as 1"

    actions = [make_priority_0, make_priority_1]


class PersonAdmin(admin.ModelAdmin):
    pass

admin.site.register(Location, LocationAdmin)
admin.site.register(Person, PersonAdmin)
