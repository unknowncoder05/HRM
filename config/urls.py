"""Main URLs module."""

# Django
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin

# Rest Framework
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

BASE_API_PATH = 'api/v1'

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),

    # Auth
    path(BASE_API_PATH+'/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(BASE_API_PATH+'/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path(BASE_API_PATH+'/user/', include(('hrm_api.users.urls', 'users'), namespace='users')),
    path(BASE_API_PATH+'/social/', include(('hrm_api.community.urls', 'users'), namespace='social')),

    path(BASE_API_PATH+'/conceptual/', include(('hrm_api.ideas.urls', 'users'), namespace='conceptual')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
