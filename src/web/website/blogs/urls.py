from django.urls import path
from .views import BlogListView, BlogPostDetailView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-list'),  # Use as_view() to connect class-based view
    path('post/<slug:slug>/', BlogPostDetailView.as_view(), name='blog_post_detail'),  # Use as_view()
]
