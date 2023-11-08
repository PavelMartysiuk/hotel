from rest_framework import serializers

from hotel_info.models import  HotelContacts

class HotelContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelContacts
        fields = "__all__"


