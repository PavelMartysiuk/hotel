from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework import mixins, generics

from hotel_info.api.v1.serializers.room_type import RoomTypeSerializer
from hotel_info.models import RoomType



class RoomTypeView(
    generics.ListAPIView,
):

    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer

