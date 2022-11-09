from django.contrib import admin
from .models import Sensor, Measurement
# Register your models here.


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_filter = ['name']
    search_fields = ['name']


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['sensor_id', 'temperature', 'measured_at', 'image']
    list_filter = ['sensor_id', 'measured_at']
    search_fields = ['sensor_id', 'measured_at']
