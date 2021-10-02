"""Django models utilities."""

# Django
from django.db import models


class DefaultModel(models.Model):
    """Comparte Ride base model.

    DefaultModel acts as an abstract base class from which every
    other model in the project will inherit. This class provides
    every table with the following attributes:
        + created (DateTime): Store the datetime the object was created.
        + updated_at (DateTime): Store the last datetime the object was modified.
    """

    created_at = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )
    updated_at = models.DateTimeField(
        'updated at',
        auto_now=True,
        help_text='Date time on which the object was last modified.'
    )

    deleted_at = models.DateTimeField(
        'deleted at',
        help_text='Date time on which the object was deleted.',
        null=True
    )

    class Meta:
        """Meta option."""

        abstract = True

        get_latest_by = 'created_at'
        ordering = ['-created_at', '-updated_at']
