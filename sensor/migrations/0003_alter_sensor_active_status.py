# Generated by Django 4.1.2 on 2022-10-21 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sensor", "0002_sensor_active_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sensor",
            name="active_status",
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
