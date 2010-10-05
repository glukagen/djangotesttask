from base.models import Location, Person
from django.contrib import admin


class LocationAdmin(admin.ModelAdmin):
    pass


class PersonAdmin(admin.ModelAdmin):
    pass


admin.site.register(Location, LocationAdmin)
admin.site.register(Person, PersonAdmin)
