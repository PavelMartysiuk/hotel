from rest_framework import serializers

from hotel_info.models import  HotelPhoto

class HotelPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelPhoto
        fields = "__all__"


