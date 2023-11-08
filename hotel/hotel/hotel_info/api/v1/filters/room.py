from django_filters import rest_framework as filters

from hotel_info.models import Room


class RoomFilter(filters.FilterSet):

    class Meta:
        model = Room
        fields = ("room_type", )
