import django_filters
from .models import TeamMember, Rank

class TeamMemberFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Search by Name')
    role = django_filters.CharFilter(lookup_expr='icontains', label='Search by Role')
    rank = django_filters.ModelChoiceFilter(queryset=Rank.objects.all(), label='Rank')
    is_active = django_filters.BooleanFilter(label='Is Active')

    class Meta:
        model = TeamMember
        fields = ['name', 'role', 'rank', 'is_active']
