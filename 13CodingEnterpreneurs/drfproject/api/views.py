from django.shortcuts import render
from django.http import JsonResponse
import json
from products.models import Product

# Create your views here.

def api_home(request,*args,**kwargs):
    #remember request is the instance of the http class. 
    #and the requests is used for the json response.
   model_data=Product.objects.all().order_by("?").first()
   data={}
   if model_data:
      data['title']=model_data.title
      data['content']=model_data.content
      return JsonResponse(data)