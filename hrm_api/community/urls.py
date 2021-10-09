"""Social Media URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import social_media as link_views

router = DefaultRouter()
router.register('link', link_views.LinkViewSet, basename='link')

urlpatterns = [
    path('', include(router.urls))
]
