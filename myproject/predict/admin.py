from django.contrib import admin
from .models import PredictionData

@admin.register(PredictionData)
class PredictionDataAdmin(admin.ModelAdmin):
    list_display = ('weather', 'road', 'time', 'package')