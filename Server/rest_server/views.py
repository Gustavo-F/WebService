import json
from . import models
from datetime import date
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse, JsonResponse


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


def get_statistics(request):
    get_date = request.GET.get('date')
    if not get_date: get_date = date.today()

    statistics = models.MeteorologicalStatistics.objects.filter(date=get_date).order_by('date')
    statistics = [obj.as_json() for obj in statistics]

    return HttpResponse(json.dumps(statistics), content_type='application/json')
