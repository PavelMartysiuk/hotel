from rest_framework.response import Response

from rest_framework import mixins, generics, status
import datetime

from hotel_info.api.v1.serializers.booking import BookingSerializer
from hotel_info.models import Booking
from django_filters.rest_framework import DjangoFilterBackend
from hotel_info.api.v1.filters.booking import BookingFilter


class BookingView(
    generics.CreateAPIView,
):

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        date = request.data.get("date")
        if Booking.objects.filter(date=date, room=request.data.get("room")).first():
            return Response({"Booking already exists for this day "}, status=status.HTTP_201_CREATED)
        return super().create(request, *args, **kwargs)


class BookingListView(
    generics.ListAPIView,
):

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BookingFilter

    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(date__gte=datetime.datetime.now().date())
        return super().list(request, *args, **kwargs)