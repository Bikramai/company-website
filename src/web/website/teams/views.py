from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import TeamMember
from .filters import TeamMemberFilter
from .models import TeamMember


# List view for team members with filtering
class TeamMemberListView(ListView):
    model = TeamMember
    context_object_name = 'team_members'
    paginate_by = 10  # Adjust pagination if needed

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team_member'] = TeamMember.objects.all()[:3]
        return context



# Detail view for individual team members
def team_member_detail(request, pk):
    team_member = TeamMember.objects.get(pk=pk)
    return render(request, 'teams/team_member_detail.html', {'team_member': team_member})
