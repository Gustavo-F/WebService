import json
from . import models
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def add_statistic(request):
    if request.POST:
        statistics = json.loads(request.POST.get('statistics'))

        meteorological_statistics = models.MeteorologicalStatistics(
            date = statistics['date'],
            hour = statistics['hour'],
            weather = statistics['weather'],
            temperature = statistics['temperature'],
        )

        meteorological_statistics.save()
    
    return JsonResponse('success', safe=False)
