"""Profile model."""

# Django
from django.db import models

# Models
from hrm_api.community.models import Feed, Link
from hrm_api.users.models import Profile

# Utilities
from hrm_api.utils.models import DefaultModel


class Organization(DefaultModel):
    """Organization model.

    A Organization is a group of peopple with a defined goals, organizations create projects
    """

    name = models.CharField(max_length=30)

    description = models.CharField(max_length=30)

    feed = models.ForeignKey(Feed, on_delete=models.CASCADE, related_name='project')

    created_by = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.SET_NULL, related_name='projects')

    social_links = models.ForeignKey(Link, blank=True, null=True, on_delete=models.SET_NULL, related_name='projects')
    
    def __str__(self):
        """Return Project's str representation."""
        return str(self.name)

