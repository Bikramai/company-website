from django.contrib import admin
from .models import TeamMember, Rank


@admin.register(Rank)
class RankAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    ordering = ('order',)


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'rank', 'role', 'is_active')
    list_filter = ('rank', 'is_active')
