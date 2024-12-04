from django.db import models


class ProjectCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class ProjectStatus(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status


class Project(models.Model):
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=255, default='default_value')
    challenge = models.TextField(max_length=255, default='default_value')
    solution = models.TextField(max_length=255, default='default_value')
    result = models.TextField(max_length=255, default='default_value')
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    status = models.ForeignKey(ProjectStatus, on_delete=models.SET_NULL, null=True, blank=True)
    image1 = models.ImageField(upload_to='projects/', blank=True, null=True)
    image2= models.ImageField(upload_to='projects/', blank=True, null=True)
    image3 = models.ImageField(upload_to='projects/', blank=True, null=True)
    qoute = models.TextField(max_length=255, default='default_value')


    def __str__(self):
        return self.title


class Client(models.Model):
    name = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='clients/', blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class ProjectClient(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_clients')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_projects')
    address = models.OneToOneField(Client, on_delete=models.CASCADE, related_name='client'),

    def __str__(self):
        return f"{self.client.name} - {self.project.title}"



