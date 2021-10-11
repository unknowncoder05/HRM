"""User models admin."""

# Django
from django.contrib import admin

# Models
from hrm_api.ideas.models import Project



@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Project model admin."""

    list_display = ('name', 'description', 'feed')
    #search_fields = ('profile__user__username', 'profile__user__email', 'profile__user__first_name', 'profile__user__last_name')