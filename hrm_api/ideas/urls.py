"""Social Media URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import question as question_views

router = DefaultRouter()
router.register('questions', question_views.QuestionViewSet, basename='questions')

urlpatterns = [
    path('', include(router.urls))
]
