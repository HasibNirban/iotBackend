from django.contrib import admin
from .models import Sensor


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ["sensor_id", "sensor_name", "sensor_type"]
    list_filter = ["sensor_type"]
    search_fields = ["sensor_name"]
