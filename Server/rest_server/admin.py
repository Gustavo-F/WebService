from . import models
from django.contrib import admin

class MeteorologicalStatisticsAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'hour', 'weather', 'temperature']
    list_display_links = ['id', 'date', 'hour', 'weather', 'temperature']

admin.site.register(models.MeteorologicalStatistics, MeteorologicalStatisticsAdmin)
