"""Social Media URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import idea as idea_views
from .views import question as question_views

router = DefaultRouter()
router.register('ideas', idea_views.IdeaViewSet, basename='ideas')
router.register('questions', question_views.QuestionViewSet, basename='questions')

urlpatterns = [
    path('', include(router.urls))
]
