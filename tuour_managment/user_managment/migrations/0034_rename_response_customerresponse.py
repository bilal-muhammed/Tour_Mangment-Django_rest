# Generated by Django 4.1.5 on 2023-03-22 07:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_managment', '0033_alter_customers_address_alter_customers_category_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Response',
            new_name='CustomerResponse',
        ),
    ]
