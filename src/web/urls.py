from django.contrib import admin

from django.urls import path, include

urlpatterns = [
    path('', include('src.web.website.urls', namespace='website')),
    path('team/', include('src.web.website.teams.urls')),
    path('project/', include('src.web.website.projects.urls')),
    path('service/', include('src.web.website.services.urls')),
    path('blog/', include('src.web.website.blogs.urls')),
    path('accounts/', include('src.web.accounts.urls', namespace='accounts')),
    path('admins/', include('src.web.admins.urls', namespace='admins')),
]