"""Profile model."""

# Django
from django.db import models

# Models
from hrm_api.community.models import Feed
from hrm_api.users.models import Profile

# Utilities
from hrm_api.utils.models import DefaultModel


class Question(DefaultModel):
    """Project model.

    A question is a sentence designed to obtein information about certain ideas
    """

    description = models.CharField(max_length=30)

    feed = models.ForeignKey(Feed, on_delete=models.CASCADE, related_name='questions')

    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='questions')

    original_questioner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='original_questions')

    original_ask_date = models.DateTimeField()

    

    def __str__(self):
        """Return Question's str representation."""
        return str(self.description)[:10]

