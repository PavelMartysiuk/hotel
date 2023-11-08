from rest_framework import serializers

from hotel_info.models import  RoomType

class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = "__all__"


