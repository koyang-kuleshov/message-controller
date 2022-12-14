from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import permissions
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi


TITLE = 'Send messages API'
DESCRIPTION = 'Mock-service for sending messages'

schema_view = get_schema_view(
        openapi.Info(
                title=TITLE,
                default_version='v1',
                description=DESCRIPTION,
                terms_of_service="https://www.google.com/policies/terms/",
                contact=openapi.Contact(email="michel@koyang-kuleshov.ru"),
                license=openapi.License(name="BSD License"),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path("api/", include(("mainapp.urls", "mainapp"), namespace="mainapp")),
    path('api/rest-auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/',
         include('dj_rest_auth.registration.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    re_path(r'^swagger/$',
            schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'),
    re_path(r'^redoc/$',
            schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc'),
]
