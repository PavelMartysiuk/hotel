from rest_framework import serializers

from hotel_info.models import  Room
from hotel_info.api.v1.serializers.room_photo import RoomPhotoSerializer

class RoomSerializer(serializers.ModelSerializer):
    photos = RoomPhotoSerializer(many=True, read_only=True, source="room_photo")
    class Meta:
        model = Room
        fields = ("id", "name", "capacity", "start_cost", "photos")


class RoomDetailsSerializer(serializers.ModelSerializer):
    photos = RoomPhotoSerializer(many=True, read_only=True, source="room_photo")

    class Meta:
        model = Room
        fields = "__all__"

