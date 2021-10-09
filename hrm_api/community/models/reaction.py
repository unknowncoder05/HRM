"""Profile model."""

# Django
from django.db import models

# Models
from hrm_api.community.models import Feed, Comment
from hrm_api.users.models import Profile

# Utilities
from hrm_api.utils.models import DefaultModel
from django_enum_choices.fields import EnumChoiceField
from enum import Enum

class ReactionTypes(Enum):
    Like = 1
    Celebrate = 2
    Love = 3
    Insightful = 4
    Curious = 4

class Reaction(DefaultModel):
    """Reaction model.

    A reaction is the way users show what an other user's actions make them feel
    """
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE, related_name='reactions')

    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='reactions')

    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reactions')

    type = EnumChoiceField(ReactionTypes, blank=True, null=True)

