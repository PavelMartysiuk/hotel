from django_filters import rest_framework as filters

from hotel_info.models import Booking


class BookingFilter(filters.FilterSet):

    class Meta:
        model = Booking
        fields = ("room", )
