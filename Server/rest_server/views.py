import json
from . import models
from django.http.request import QueryDict
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse, JsonResponse


@csrf_exempt
def add_statistic(request):
    status_code = 405
    response_message = {'message': f'405 - Method {request.method} Not Allowed.'}

    if request.POST:
        statistics = json.loads(request.POST.get('statistics'))
    
        if not statistics:
            status_code = 400 
            response_message = {'message': 'Data not sent.'}  
        else: 
            meteorological_statistics = models.MeteorologicalStatistics(
                date = statistics['date'],
                hour = statistics['hour'],
                weather = statistics['weather'],
                temperature = statistics['temperature'],
            )
            meteorological_statistics.save()

            status_code = 200
            response_message = {'message': 'Stat successfully saved.'}
    
    response = JsonResponse(response_message, safe=False)
    response.status_code = status_code
    return response


@csrf_exempt
def get_statistics(request):
    status_code = 405
    response_message = {'message': f'405 - Method {request.method} Not Allowed.'}

    if request.method == 'GET':
        date = request.GET.get('date')
        
        if not date:
            statistics = models.MeteorologicalStatistics.objects.order_by('-id')
        else:
            statistics = models.MeteorologicalStatistics.objects.filter(date=date).order_by('-id')

        statistics = [obj.as_json() for obj in statistics]
        status_code = 200
         
    response = JsonResponse(
        statistics if status_code == 200 else response_message,
        safe=False
    )
    
    response.status_code = status_code
    return response


@csrf_exempt
def delete_stat(request, pk):
    status_code = 405
    response_message = {'message': f'405 - Method {request.method} Not Allowed.'}

    if request.method == 'DELETE':
        try:
            stat = get_object_or_404(models.MeteorologicalStatistics, pk=pk)
            stat.delete()

            status_code = 200
            response_message['message'] = 'Statistic deleted successfully!'
        except:
            status_code = 404
            response_message['message'] = 'Stat not found.'

    response = JsonResponse(response_message, safe=False)
    response.status_code = status_code
    return response


@csrf_exempt
def update_stat(request, pk):
    status_code = 405
    response_message = {'message': f'405 - Method {request.method} Not Allowed.'}

    if request.method == 'PUT':
        try:
            stat = get_object_or_404(models.MeteorologicalStatistics, pk=pk)
            put_params = json.loads(QueryDict(request.body)['statData'])

            stat.date = put_params['date']
            stat.hour = put_params['hour']
            stat.weather = put_params['weather']
            stat.temperature = put_params['temperature']
            stat.save()

            status_code = 200
            response_message['message'] = 'Stat updated successfully!'
        except:
            status_code = 404
            response_message['message'] = 'Stat not found.'

    response = JsonResponse(response_message, safe=False)
    response.status_code = status_code
    return response
