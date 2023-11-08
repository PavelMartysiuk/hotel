from rest_framework import serializers

from hotel_info.models import  Hotel
from hotel_info.api.v1.serializers.hotel_contacs import HotelContactsSerializer
from hotel_info.api.v1.serializers.hotel_photo import HotelPhotoSerializer

class HotelSerializer(serializers.ModelSerializer):
    contacts = HotelContactsSerializer(many=True, read_only=True, source='hotel_contacts')
    photos = HotelPhotoSerializer(many=True, read_only=True, source="hotel_photo")
    class Meta:
        model = Hotel
        fields = "__all__"


