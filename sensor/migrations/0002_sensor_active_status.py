# Generated by Django 4.1.2 on 2022-10-20 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sensor", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="sensor",
            name="active_status",
            field=models.BooleanField(default=False),
        ),
    ]
