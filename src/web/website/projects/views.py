from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Project, ProjectCategory
from .forms import ProjectFilterForm


def project_list(request):
    # Initialize filter form with GET data
    filter_form = ProjectFilterForm(request.GET or None)

    # Start with all projects
    projects = Project.objects.all()

    # Apply filtering based on form data
    if filter_form.is_valid():
        category = filter_form.cleaned_data.get('category')
        status = filter_form.cleaned_data.get('status')
        is_featured = filter_form.cleaned_data.get('is_featured')

        if category:
            projects = projects.filter(category=category)
        if status:
            projects = projects.filter(status=status)
        if is_featured:
            projects = projects.filter(is_featured=True)

    # Apply pagination
    paginator = Paginator(projects.order_by('-created_at'), 10)  # 10 projects per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'filter_form': filter_form,
        'projects': page_obj,
    }

    return render(request, 'website/project_list.html', context)


def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    print(project ,"asas")
    return render(request, 'website/project-details.html', {'project': project})




