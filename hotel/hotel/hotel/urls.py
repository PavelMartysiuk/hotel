from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib import admin
from hotel import settings

from core.swagger.view import schema_view
from hotel_info.api.v1.views.hotel import HotelView
from hotel_info.api.v1.views.room_type import RoomTypeView
from hotel_info.api.v1.views.room import RoomView, RoomDetailsView
from hotel_info.api.v1.views.booking import BookingView, BookingListView

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('api/v1/hotel/', HotelView.as_view()),
    path('api/v1/room-type/', RoomTypeView.as_view()),
    path('api/v1/room/', RoomView.as_view()),
    path('api/v1/room/<int:pk>/', RoomDetailsView.as_view()),
    path('api/v1/booking/', BookingView.as_view()),
    path('api/v1/booking/list/', BookingListView.as_view())

]

urlpatterns += (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
                static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
if settings.USE_SWAGGER:
    urlpatterns.extend((
        re_path(r'api/swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        path(r'api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path(r'api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ))

admin.site.site_header = 'Hotel Admin Panel'
admin.site.site_title = 'Hotel'
