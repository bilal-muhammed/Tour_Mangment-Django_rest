# Generated by Django 4.1.5 on 2023-03-09 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trippens', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='tour',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='trippens.trippenstour'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Tour',
        ),
    ]
