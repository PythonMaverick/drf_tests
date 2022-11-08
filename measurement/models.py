from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.TextField(max_length=25)
    description = models.TextField(max_length=100)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    measured_at = models.DateField(auto_now=True)
    image = models.ImageField(null=True, upload_to='media')
