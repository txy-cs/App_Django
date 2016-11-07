from django.shortcuts import render
from django.http import HttpResponse
import json
import time

# Create your views here.
def login(request):
    message = { "datas": [],
                "time": time.strftime('%Y-%m-%d-%H-%M-%S'),
                "status_no": 0,
                "status_msg": ""
            }
    user=request.GET['user']
    password=request.GET['password']
    if user!="123":
        message["status_no"]=1000
    elif user=="123" and password!="123":
        message["status_no"]=1001
    else:
        message["status_no"]="1002"
    
    return HttpResponse(json.dumps(message))
