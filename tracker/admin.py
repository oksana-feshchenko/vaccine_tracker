from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from tracker.models import Parent, Child, Vaccine, Vaccination, Complication


admin.site.unregister(Group)


@admin.register(Parent)
class Parent(UserAdmin):
    pass


@admin.register(Child)
class Child(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "birth_date", "gender"]
    list_filter = ["parent__last_name"]
    search_fields = ["first_name", "last_name"]


@admin.register(Vaccine)
class Vaccine(admin.ModelAdmin):
    list_display = ["name", "age_for_first_dose_days", "number_of_doses"]
    list_filter = ["name"]
    search_fields = ["name"]


@admin.register(Vaccination)
class Vaccination(admin.ModelAdmin):
    list_display = ["get_name", "date_vaccination"]
    list_filter = ["child__last_name"]
    search_fields = ["get_name"]

    def get_name(self, obj):
        return obj.vaccine.name

    get_name.admin_order_field = "vaccine "
    get_name.short_description = "Vaccine"


@admin.register(Complication)
class Complication(admin.ModelAdmin):
    list_display = ["description", "date_occurrence"]
    list_filter = ["date_occurrence"]
    search_fields = ["description"]
