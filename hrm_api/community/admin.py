"""User models admin."""

# Django
from django.contrib import admin

# Models
from hrm_api.community.models import Link, Feed, Comment, Reaction



@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    """Link model admin."""

    list_display = ('description', 'url')
    search_fields = ('profile__user__username', 'profile__user__email', 'profile__user__first_name', 'profile__user__last_name')

@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    """Feed model admin."""
    list_display = ('id',)# , 'idea', 'question'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Comment model admin."""

    list_display = ('id', 'feed', 'parent', 'created_by')

@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    """Reaction model admin."""

    list_display = ('id', 'feed', 'comment', 'created_by', 'type')