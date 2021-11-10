import json

from django.http import response
from . import models
from django.shortcuts import get_object_or_404
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


@csrf_exempt
def get_statistics(request):
    date = request.GET.get('date')
    if not date:
        statistics = models.MeteorologicalStatistics.objects.order_by('-date')[:20]
    else:
        statistics = models.MeteorologicalStatistics.objects.filter(date=date).order_by('-date')

    statistics = [obj.as_json() for obj in statistics]

    return HttpResponse(json.dumps(statistics), content_type='application/json')


@csrf_exempt
def delete_stat(request, pk):
    status_code = 403
    response_message = {'message': 'Unauthorized access.'}

    if request.method == 'DELETE':
        stat = get_object_or_404(models.MeteorologicalStatistics, pk=pk)
        print(f'\n{stat}\n')
        stat.delete()

        status_code = 200
        response_message['message'] = 'Statistic deleted successfully!'

    response = JsonResponse(response_message, safe=False)
    response.status_code = status_code
    return response
