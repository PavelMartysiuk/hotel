# Generated by Django 4.1.2 on 2023-11-06 20:57

import core.models.utils
import core.validators.model_validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HotelContacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=35)),
                ('contact_type', models.CharField(choices=[('phone', 'phone'), ('email', 'email')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, null=True, upload_to=core.models.utils.ModelMethods.get_upload_path, validators=[core.validators.model_validators.SizeValidators.image_size_validator])),
                ('description', models.TextField()),
                ('start_cost', models.FloatField()),
                ('size', models.FloatField()),
                ('capacity', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, null=True, upload_to=core.models.utils.ModelMethods.get_upload_path, validators=[core.validators.model_validators.SizeValidators.image_size_validator])),
                ('description', models.TextField()),
                ('start_cost', models.FloatField()),
                ('end_cost', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='RoomPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to=core.models.utils.ModelMethods.get_upload_path, validators=[core.validators.model_validators.SizeValidators.image_size_validator])),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_photo', to='hotel_info.room')),
            ],
        ),
        migrations.CreateModel(
            name='HotelPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=core.models.utils.ModelMethods.get_upload_path, validators=[core.validators.model_validators.SizeValidators.image_size_validator])),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_photo', to='hotel_info.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('guest', models.EmailField(max_length=255)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='hotel_info.room')),
            ],
        ),
    ]
