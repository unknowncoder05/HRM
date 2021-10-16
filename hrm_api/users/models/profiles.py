"""Profile model."""

# Django
from django.db import models

# Utilities
from hrm_api.utils.models import DefaultModel
from hrm_api.users.models import User


class Profile(DefaultModel):
    """Profile model.

    A profile holds a user's public data like biography, picture,
    and statistics.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )

    biography = models.TextField(max_length=500, blank=True)

    is_public = models.BooleanField(
        'is public',
        default=True,
        help_text='Set to true if user wants profile to be visible.'
    )

    # Stats
    """reputation = models.FloatField(
        default=3.0,
        help_text="User's reputation based on the questions asked and comments posted."
    )"""

    def __str__(self):
        """Return user's str representation."""
        return str(self.user)
    
    def count_ideas(self):
        return self.ideas.count()
    
    def count_questions(self):
        return self.questions.count()


