"""User models admin."""

# Django
from django.contrib import admin

# Models
from hrm_api.community.models import Link



@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    """Link model admin."""

    list_display = ('description', 'url')
    search_fields = ('profile__user__username', 'profile__user__email', 'profile__user__first_name', 'profile__user__last_name')