import json
import time
import socket
import random

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

def Main():
    host = '127.0.0.1'
    port = random.randrange(2000, 7999)

    collector_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    collector_socket.bind((host, port))

    while(True):
        meteorological_statistics = {
            'temperature': round(random.uniform(-5, 40), 1),
            'date': random_date('01/01/2012', '05/11/2021', '%d/%m/%Y', random.random()),
            'hour': random_hour(),
        }            

        print(json.dumps(meteorological_statistics))
        time.sleep(10)

if __name__ == '__main__':
    Main()