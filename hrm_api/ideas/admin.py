"""User models admin."""

# Django
from django.contrib import admin

# Models
from hrm_api.ideas.models import Question



@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Question model admin."""

    list_display = ('description', 'feed', 'created_by', 'original_questioner', 'original_ask_date')
    #search_fields = ('profile__user__username', 'profile__user__email', 'profile__user__first_name', 'profile__user__last_name')