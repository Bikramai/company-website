from django.contrib import admin
from .models import ProjectCategory, Project, Client, ProjectClient, ProjectStatus


class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


class ProjectStatusAdmin(admin.ModelAdmin):
    list_display = ('status',)
    search_fields = ('status',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'is_featured', 'created_at')
    list_filter = ('category', 'status', 'is_featured')
    search_fields = ('title', 'description')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'website')
    search_fields = ('name', 'website')


class ProjectClientAdmin(admin.ModelAdmin):
    list_display = ('client', 'project')
    search_fields = ('client__name', 'project__title')


# Register your models here
admin.site.register(ProjectCategory, ProjectCategoryAdmin)
admin.site.register(ProjectStatus, ProjectStatusAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(ProjectClient, ProjectClientAdmin)
