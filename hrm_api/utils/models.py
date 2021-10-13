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

    def non_deleted(self):
        return self.objects.filter(deleted_at__isnull=False)

    class Meta:
        """Meta option."""

        abstract = True

        get_latest_by = 'created_at'
        ordering = ['-created_at', '-updated_at']

def save_save(model):
    try:    
        model.save()
    except Exception as e:
        print(print(model.__dict__), e)
        raise Exception(e)