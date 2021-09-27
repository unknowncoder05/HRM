"""Profile model."""

# Django
from django.db import models

# Utilities
from hrm_api.utils.models import DefaultModel


class Link(DefaultModel):
    """Link model.

    A link can be used either by profiles or projects 
    for them to show their external social platforms.
    
    Warning: This links should be audited often.
    """

    name = models.CharField(max_length=30, blank=False)
    url = models.URLField(max_length=30, blank=False)

    def __str__(self):
        """Return link's str representation."""
        return str(self.name)

