from django.shortcuts import render
from .models import *
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse

# Create your views here.

# Model Object -single object data getting


def student_detail(request,pk):
    stu=Student.objects.get(id=pk)
    print('printing stu',stu)
    serializers=StudentSerializer(stu) #to get many data or objects at the same time. 
    print('printing serializers',serializers)
    print('printing serializers.data',serializers.data)
   
    return JsonResponse(serializers.data,safe=False)

# from above api we are getting the data 
# {
#   "name": "yash",
#   "roll": 21,
#   "city": "Kota"
# }


def student_list(request):
    stu=Student.objects.all()
    print('printing stu',stu)
    serializers=StudentSerializer(stu,many=True) #to get many data or objects at the same time. 
    print('printing serializers',serializers)
    print('printing serializers.data',serializers.data)
    return JsonResponse(serializers.data,safe=False)

#to get the all data into the json format you must set the many property into true .  [
#   {
#     "name": "yash",
#     "roll": 21,
#     "city": "Kota"
#   },
#   {
#     "name": "Mudit",
#     "roll": 43,
#     "city": "Jaipur"
#   },
#   {
#     "name": "Rajat Jain",
#     "roll": 87,
#     "city": "Ranchi"
#   }
# ]