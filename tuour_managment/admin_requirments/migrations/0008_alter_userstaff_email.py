# Generated by Django 4.1.5 on 2023-03-15 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_requirments', '0007_rooms_place_vehicle_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstaff',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
    ]
