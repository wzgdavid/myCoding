# encoding: utf-8
'''
file:views/main.py
'''
import time
from django.http import HttpResponse
import json


def api(request):
    data = {}
    now = int(time.time())
    data['data'] = {
        'server_now':now,
    }

    params = request.REQUEST

    # 浏览器  访问http://127.0.0.1:8000/api/?name=xxx
    data['request_params'] = dict(params)

    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/x-javascript',
    )


def api2(request):
    data = {}
    now = int(time.time())
    data['data'] = {
        'server_now':now,
        'hello': 'django',
    }

    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/x-javascript',
    )