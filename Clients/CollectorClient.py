import os
import json
import time
import random
import requests

def random_date(start, end, format, prop):
    end_time = time.mktime(time.strptime(end, format))
    start_time = time.mktime(time.strptime(start, format))

    ptime = start_time + prop * (end_time - start_time)
    return time.strftime(format, time.localtime(ptime))

def random_hour():
    hour = random.randrange(0, 24)
    minute = random.randint(0, 60)
    second = random.randrange(0, 60)

    return (f'{"0" + str(hour) if hour < 10 else hour}:'
            f'{"0" + str(minute) if minute < 10 else minute}:'
            f'{"0" + str(second) if second < 10 else second}')

def random_weather():
    value = str(random.randint(1, 3))
    return {
        '1': 'Rainy',
        '2': 'Sunny',
        '3': 'Cloudy',
    }[value]

def send_statistics(client, meteorological_statistics):
    url = 'http://127.0.0.1:8000/add_statistic/'
    
    response = client.post(url, data=dict(
        statistics=meteorological_statistics,
        next='/',
    ))
    
    print(response)

def Main():
    client = requests.session()

    while(True):
        meteorological_statistics = {
            'weather': random_weather(),
            'temperature': round(random.uniform(-5, 40), 1),
            'date': random_date('2021-01-01', '2021-11-01', '%Y-%m-%d', random.random()),
            'hour': random_hour(),
        }            

        send_statistics(client, json.dumps(meteorological_statistics))
        time.sleep(10)

if __name__ == '__main__':
    Main()