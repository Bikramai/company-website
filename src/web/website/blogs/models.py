from django.db import models
from django.utils import timezone


# Category model for blog categories
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


# Blog Post model
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author_name = models.CharField(max_length=100, null=True)  # Allow null temporarily

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)

    tags = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Tag model for blog post tags
class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
