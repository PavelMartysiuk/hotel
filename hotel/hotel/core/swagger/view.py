from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from hotel import settings


schema_view = get_schema_view(
   openapi.Info(
      title='Udi snippets API',
      default_version='v1',
      description='API description',
      contact=openapi.Contact(email='udi@innowise-group.com'),
      license=openapi.License(name='udi-group License'),
   ),
   url=settings.SWAGGER_LINK,
   public=True,
   permission_classes=(permissions.AllowAny,),
)