from django.shortcuts import render
from django.http import HttpResponse
import json
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

#def getProduct(request):
#    fcid=request.GET['fcid']
#    scid=request.GET['scid']
#    l=dict()
#    for e in product.objects.filter(first_category_id=fcid).filter(second_category=scid):
#        l[e.]
    