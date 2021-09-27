"""Users URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import link as link_views

router = DefaultRouter()
router.register(r'social-links', link_views.LinkViewSet, basename='link')

urlpatterns = [
    path('', include(router.urls))
]
