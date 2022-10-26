from django.db import models


class Sensor(models.Model):

    CHOICES = [
        (1, "TEMPERATURE_SENSOR"),
        (2, "PRESSURE_SENSOR"),
        (3, "HUMIDITY_SENSOR"),
        (4, "FLUID_SENSOR"),
        (5, "PIEZO_SENSOR"),
    ]

    sensor_id = models.CharField(max_length=100, unique=True)
    sensor_name = models.CharField(max_length=100)
    sensor_type = models.IntegerField(choices=CHOICES)
    sensor_value = models.CharField(max_length=100)
    sensor_data = models.CharField(max_length=100)

    def __str__(self):
        return self.sensor_id
