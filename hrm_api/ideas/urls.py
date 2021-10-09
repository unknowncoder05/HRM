"""Social Media URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import project as project_views

router = DefaultRouter()
router.register('project', project_views.ProjectViewSet, basename='project')

urlpatterns = [
    path('', include(router.urls))
]
