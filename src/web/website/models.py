from django.db import models

class Testimonials(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonials/')
    is_active = models.BooleanField(default=False)


class Stats(models.Model):
    experience = models.CharField(max_length=100)
    projects_completed = models.CharField(max_length=100)
    team_members = models.CharField(max_length=100)
    awards = models.CharField(max_length=100)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_num = models.CharField(max_length=100)
    message = models.TextField()