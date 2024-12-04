from django.db import models


class Rank(models.Model):
    name = models.CharField(max_length=50, unique=True, help_text="Rank or position title.")
    order = models.PositiveIntegerField(default=0, help_text="Order of the rank, lower numbers appear first.")

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Rank"
        verbose_name_plural = "Ranks"

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    rank = models.ForeignKey(Rank, on_delete=models.SET_NULL, null=True, blank=True,
                             help_text="Select the rank or position of the team member.")
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='team_images/', help_text="Upload a profile image.")
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    achievements = models.TextField(blank=True, null=True, help_text="Mention key achievements or recognitions.")
    display_order = models.PositiveIntegerField(default=0, help_text="Order of appearance in the team listing.")
    date_joined = models.DateField(blank=True, null=True, help_text="Date when the team member joined.")
    is_active = models.BooleanField(default=True, help_text="Set to False if the member is no longer part of the team.")

    def __str__(self):
        return f"{self.name} - {self.rank} - {self.role}"

    class Meta:
        ordering = ['display_order', 'rank__order', 'name']
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"
