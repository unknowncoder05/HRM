"""Profile model."""

# Django
from django.db import models

# Models
from hrm_api.community.models import Feed
from hrm_api.ideas.models import Question, Organization
from hrm_api.users.models import Profile
# Utilities
from hrm_api.utils.models import DefaultModel


class Project(DefaultModel):
    """Project model.

    A project is an implementation designed to solve a question
    """

    name = models.CharField(max_length=30)

    description = models.CharField(max_length=30)

    question = models.ManyToManyField(Question, related_name='projects')

    feed = models.ForeignKey(Feed, on_delete=models.CASCADE, related_name='project')

    organization = models.ForeignKey(Organization, blank=True, null=True, on_delete=models.SET_NULL, related_name='projects')

    created_by = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.SET_NULL, related_name='projects')
    
    def __str__(self):
        """Return Project's str representation."""
        return str(self.name)

