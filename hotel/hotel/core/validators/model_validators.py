import datetime

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


phone_number_validator = RegexValidator(
    regex='^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$',
    message='Please enter phone number.',
    code='nomatch',
)


class SizeValidators:
    @staticmethod
    def file_size_validator(value):
        limit = 2 * 1024 * 1024
        if value.size > limit:
            raise ValidationError('File too large. Size should not exceed 2 MB.')

    @staticmethod
    def image_size_validator(value):
        limit = 10 * 1024 * 1024
        if value.size > limit:
            raise ValidationError('File too large. Size should not exceed 10 MB.')


class DateValidators:
    @staticmethod
    def date_in_past_validator(value):
        if value < datetime.date.today():
            raise ValidationError('The date cannot be in the past.')

    @staticmethod
    def date_in_future_validator(value):
        if value > datetime.date.today():
            raise ValidationError('The date cannot be in the future')
