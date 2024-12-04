from django.urls import path
from .views import TeamMemberListView, team_member_detail


app_name = 'teams'
urlpatterns = [
    path('member/', TeamMemberListView.as_view(), name='team-list'),
    path('team/<int:pk>/', team_member_detail, name='team-member-detail'),
]
