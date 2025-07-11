from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="LIMS-GT API",
        default_version='v1',
        description="API documentation for Lab Information Management System for Genotyping",
        contact=openapi.Contact(email="Henry.Mwaka@naro.go.ug"),
        license=openapi.License(name="Apache 2.0"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('labcore.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    # Swagger & ReDoc routes
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
