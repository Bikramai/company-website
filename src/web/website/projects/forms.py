from django import forms
from .models import ProjectCategory, ProjectStatus


class ProjectFilterForm(forms.Form):
    category = forms.ModelChoiceField(
        queryset=ProjectCategory.objects.all(),
        required=False,
        empty_label="All Categories",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    status = forms.ModelChoiceField(
        queryset=ProjectStatus.objects.all(),
        required=False,
        empty_label="All Statuses",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    is_featured = forms.BooleanField(
        required=False,
        label="Featured Only",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
