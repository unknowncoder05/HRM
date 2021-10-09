"""Profile model."""

# Django
from django.db import models

# Utilities
from hrm_api.utils.models import DefaultModel


class Feed(DefaultModel):
    """Feed model.

    The feed object links user interactions with other users actions
    """

