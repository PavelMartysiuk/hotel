from rest_framework.response import Response

from rest_framework import mixins, generics, status

from hotel_info.api.v1.serializers.booking import BookingSerializer
from hotel_info.models import Booking



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

