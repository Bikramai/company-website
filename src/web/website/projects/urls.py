# urls.py
from django.urls import path
from . import views


app_name = 'project'

urlpatterns = [
    path('lists/', views.project_list, name='project_list'),
    path('detail/<int:project_id>/', views.project_detail, name='project-detail'),
]
