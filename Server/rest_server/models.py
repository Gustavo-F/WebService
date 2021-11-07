from django.db import models

class MeteorologicalStatistics(models.Model):
    date = models.DateField()
    hour = models.TimeField()
    weather = models.CharField(max_length=100)
    temperature = models.DecimalField(decimal_places=1, max_digits=3)

    def as_json(self):
        return dict(
            id = self.id,
            date = str(self.date),
            hour = str(self.hour),
            weather = self.weather,
            temperature = str(self.temperature),
        )
