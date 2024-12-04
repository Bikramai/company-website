from django.shortcuts import render
from django.views.generic import TemplateView

from .blogs import models as blog_models
from .blogs.models import BlogPost
from .models import Testimonials, Stats
from .services.models import Service
from .teams.models import TeamMember
from .forms import ContactForm


# Create your views here.
class HomeView(TemplateView):
    template_name = 'website/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.filter(is_active=True)[:4]
        context['testimonial'] = Testimonials.objects.filter(is_active=True).first()
        context['stats'] = Stats.objects.all().first()
        context['blog_posts'] = blog_models.BlogPost.objects.all().order_by('-created_at')[:3]

        return context


def team_view(request):
    return render(request, 'website/team.html')


from django.core.paginator import Paginator


def blog_view(request):
    posts = BlogPost.objects.all()
    paginator = Paginator(posts, 4)  # Adjust number of posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'website/blog.html', {'posts': page_obj})  # Use page_obj for pagination


def project_view(request):
    return render(request, 'website/project.html')


def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'website/contact.html', {'form': form, 'success': True})
        else:
            return render(request, 'website/contact.html', {'form': form, 'success': False})
    return render(request, 'website/contact.html', {'form': form})

def about_view(request):
    testimonials = Testimonials.objects.filter(is_active=True)[:3]
    member = TeamMember.objects.all()[:4]
    return render(request, 'website/about.html', {'testimonials': testimonials, 'members': member})


def service_view(request):
    return render(request, 'website/service.html')


def service_details_view(request):
    return render(request, 'website/service-details.html')


def blog_details_view(request):
    return render(request, 'website/blog-details.html')


def project_details_view(request):
    return render(request, 'website/project-details.html')
