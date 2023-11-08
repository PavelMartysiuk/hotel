from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework import mixins, generics

from hotel_info.api.v1.serializers.hotel import HotelSerializer
from hotel_info.models import Hotel



class HotelView(
    generics.ListAPIView,
):

    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.first()
        serializer = self.get_serializer(queryset, )
        return Response(serializer.data)

