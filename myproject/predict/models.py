from django.db import models

# Create your models here.

class PredictionData(models.Model):
    WEATHER_CHOICES = [
        (0, '晴れ'),
        (1, '曇り'),
        (2, '雨'),
    ]

    weather = models.IntegerField(choices=WEATHER_CHOICES)
    road = models.IntegerField()
    time = models.IntegerField()
    package = models.IntegerField()

    def __str__(self):
        return f"Weather: {self.get_weather_display()}, Road: {self.road}, Time: {self.time}, Package: {self.package}"