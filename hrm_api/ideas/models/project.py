"""Profile model."""

# Django
from django.db import models

# Models
from hrm_api.community.models import Feed
from hrm_api.ideas.models import Question
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
    

    def __str__(self):
        """Return Project's str representation."""
        return str(self.name)

