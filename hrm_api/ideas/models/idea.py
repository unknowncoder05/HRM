"""Profile model."""

# Django
from django.db import models

# Models
from hrm_api.community.models import Feed
from hrm_api.users.models import Profile
from hrm_api.ideas.models import Question

# Utilities
from hrm_api.utils.models import DefaultModel


class Idea(DefaultModel):
    """Idea model.

    Ideas are the building block for questions to rise and for organizations and projects to focus on
    """
    questions =  models.ManyToManyField(Question, related_name='child_ideas')

    name = models.CharField(unique=True, max_length=30)

    description = models.CharField(unique=True, max_length=300)

    feed = models.ForeignKey(Feed, blank=True, null=True, on_delete=models.SET_NULL, related_name='ideas')

    created_by = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.SET_NULL, related_name='ideas')

    original_thinker = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.SET_NULL, related_name='original_ideas')

    original_thinking_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        """Return Question's str representation."""
        return str(self.description)[:10]

