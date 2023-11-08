from django.contrib import admin



from .models import Hotel, HotelContacts, HotelPhoto, RoomType, Room, RoomPhoto

admin.site.register(Hotel)
admin.site.register(HotelContacts)
admin.site.register(HotelPhoto)
admin.site.register(RoomType)
admin.site.register(Room)
admin.site.register(RoomPhoto)