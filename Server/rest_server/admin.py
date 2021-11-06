from . import models
from django.contrib import admin

class MeteorologicalStatisticsAdmin(admin.ModelAdmin):
    display_list = ['id', 'date', 'hour', 'weather', 'temperature']
    display_list_links = ['id', 'date', 'hour', 'weather', 'temperature']

admin.site.register(models.MeteorologicalStatistics, MeteorologicalStatisticsAdmin)
