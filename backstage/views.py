#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import json,time
from backstage.models import first_category,second_category,product

# Create your views here.

def getFirstCategory(request):
    l=dict()
    for e in first_category.objects.all():
        l[e.fcid]=e.name
    return HttpResponse(json.dumps(l))

def getSecondCategory(request):
    fcid=request.GET['fcid']
    l=dict()
    for e in second_category.objects.filter(first_category_id=fcid):
        l[e.scid]=e.name
    return HttpResponse(json.dumps(l))

def getProduct(request):
    scid=request.GET['scid']
    l=dict()
    for e in product.objects.filter(second_category=scid):
        temp=dict()
        temp['name']=e.name
        temp['price']=e.price
        temp['num']=e.num
        temp['image_link']=e.image_link
        l[e.pid]=temp
    return HttpResponse(json.dumps(l))
    
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
