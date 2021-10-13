"""Profile model."""

# Django
from django.db import models

# Models
from hrm_api.users.models import Profile

# Utilities
from hrm_api.utils.models import DefaultModel


class Link(DefaultModel):
    """Link model.

    A link can be used either by profiles or projects 
    for them to show their external social platforms.
    
    Warning: This links should be audited often.
    """

    description = models.CharField(max_length=30)

    url = models.URLField(max_length=60)

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='social_links')

    def __str__(self):
        """Return link's str representation."""
        return str(self.description)

