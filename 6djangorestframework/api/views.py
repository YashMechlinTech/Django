from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from products.models import Products
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

@api_view(['GET', 'POST'])
def api_home(request,*args,**kwargs):
    # model_data=Products.objects.all() .order_by("?").first()
  
    # if model_data is None:
    #     return JsonResponse({"message":"No json response is availiable since model data is not present"})
    # # data={
    # #     "title": model_data.title,
    # #     "content": model_data.content,
    # #     "price": model_data.price,
    # # } #this is the dictionary
    # data=model_to_dict(model_data)#same work as above 

    # # Debugging purpose to see the JSON data

    # return Response(data)
    product=Products.objects.all()
    serializer=ProductSerializer(product,many=True)
    return Response(serializer.data)