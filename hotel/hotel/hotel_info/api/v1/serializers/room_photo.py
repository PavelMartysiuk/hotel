from rest_framework import serializers

from hotel_info.models import  RoomPhoto

class RoomPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomPhoto
        fields = "__all__"


