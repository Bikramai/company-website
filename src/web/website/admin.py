from django.contrib import admin

from . models import (
    Testimonials, Stats, Contact
)


@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'position', 'image')


@admin.register(Stats)
class StatsAdmin(admin.ModelAdmin):
    list_display = ('experience', 'projects_completed', 'team_members', 'awards')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email', 'phone_num', 'message')