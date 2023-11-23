from rest_framework.response import Response

from rest_framework import mixins, generics, status
import datetime

from hotel_info.api.v1.serializers.booking import BookingSerializer
from hotel_info.models import Booking
from django_filters.rest_framework import DjangoFilterBackend
from hotel_info.api.v1.filters.booking import BookingFilter
import datetime

class BookingView(
    generics.CreateAPIView,
):

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        start_date = request.data.get("start_date")
        end_date = request.data.get("end_date")
        if start_date > end_date:
            return Response({"Start date < end date"}, status=status.HTTP_400_BAD_REQUEST)
        if datetime.datetime.strptime(start_date, "%Y-%m-%d").date()    < datetime.datetime.now().date():
            return Response({"Date can't be in past"}, status=status.HTTP_400_BAD_REQUEST)
        if Booking.objects.filter(start_date__range=(start_date, end_date), end_date__range=(start_date, end_date), room=request.data.get("room")).first():
            return Response({"Booking already exists for this day "}, status=status.HTTP_400_BAD_REQUEST)
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