from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import BlogPost


# Class-based view to list all blog posts
class BlogListView(ListView):
    model = BlogPost
    template_name = 'website/blog.html'  # Specify your template name
    context_object_name = 'blogs'

    def get_queryset(self):
        # Only display active services
        return  BlogPost.objects.filter(is_active=True)
    # This is the variable name that will be passed to the template


# Class-based view to detail a single blog post
class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'website/blog-details.html'  # Specify your template name
    context_object_name = 'post'  # This is the variable name that will be passed to the template

