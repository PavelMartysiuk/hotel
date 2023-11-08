from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework import mixins, generics

from hotel_info.api.v1.serializers.room import RoomSerializer, RoomDetailsSerializer
from hotel_info.models import Room

from django_filters.rest_framework import DjangoFilterBackend
from hotel_info.api.v1.filters.room import RoomFilter


class RoomView(
    generics.ListAPIView,
    generics.RetrieveAPIView,
):

    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RoomFilter

class RoomDetailsView(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = Room.objects.all()
    serializer_class = RoomDetailsSerializer
