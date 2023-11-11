import os

from django.db import models

from core.models.utils import ModelMethods
from core.validators.model_validators import SizeValidators
from core.enum.contact_type import ContactType


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class HotelContacts(models.Model):
    contact = models.CharField(max_length=35)
    contact_type = models.CharField(choices=ContactType.items(), max_length=10)
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE, related_name='hotel_contacts')

class HotelPhoto(models.Model):
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE, related_name='hotel_photo')
    photo = models.ImageField(
        null=True,
        upload_to=ModelMethods.get_upload_path,
        blank=True,
        validators=[SizeValidators.image_size_validator],
    )
    def image_path(self):
        return os.path.join(f'hotel_photo/{self.id}')


class RoomType(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(null=True,
                              upload_to=ModelMethods.get_upload_path,
                              blank=True,
                              validators=[SizeValidators.image_size_validator], )
    description = models.TextField()
    start_cost = models.FloatField()
    end_cost = models.FloatField()

    def image_path(self):
        return os.path.join(f'room_type_photo/{self.id}')

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    cost = models.FloatField()
    size = models.FloatField()
    capacity = models.IntegerField()
    room_type = models.ForeignKey('RoomType', on_delete=models.CASCADE, related_name='rooms')

    def __str__(self):
        return self.name


class RoomPhoto(models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE, related_name='room_photo')
    photo = models.ImageField(
        null=False,
        upload_to=ModelMethods.get_upload_path,
        blank=False,
        validators=[SizeValidators.image_size_validator],
    )
    def image_path(self):
        return os.path.join(f'room__photo/{self.id}')


class Booking(models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE, related_name='booking')
    date = models.DateField(null=False, blank=False)
    guest = models.EmailField(max_length=255)
