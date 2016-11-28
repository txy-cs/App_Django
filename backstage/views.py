#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import json,time
from backstage.models import first_category,second_category,product,order,order_product,user,address

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

def getProductDetail(request):
    pid=request.GET['pid']
    p=product.objects.get(pid=pid)
    l=dict()
    l['pid']=p.pid
    l['name']=p.name
    l['price']=p.price
    l['image_link']=p.image_link
    return HttpResponse(json.dumps(l))

def getOrder(request):# 根据用户返回订单
    uid=request.GET['uid']
    l=dict()
    for e in order.objects.filter(user_id=uid):
        temp=dict()
        temp['price']=e.price
        temp['time']=e.time.strftime("%Y-%m-%d %H:%M:%S")
        temp['status']=e.status
        temp['address']=address.objects.get(aid=e.address_id).addr
        temp2=dict()
        for sube in order_product.objects.filter(order_id=e.oid):
            temp2[sube.product_id]=sube.pnum
        temp['products']=temp2
        l[e.oid]=temp
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
