# Generated by Django 4.1.2 on 2023-11-07 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelcontacts',
            name='hotel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='hotel_contacts', to='hotel_info.hotel'),
            preserve_default=False,
        ),
    ]
