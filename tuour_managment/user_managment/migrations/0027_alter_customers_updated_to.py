# Generated by Django 4.1.5 on 2023-03-10 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_managment', '0026_leaverequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='updated_to',
            field=models.DateField(null=True),
            preserve_default=False,
        ),
    ]
