from django.http import JsonResponse
import io
from rest_framework.parsers import JSONParser
from .serializers import *
from .models import Student
from .serializers import StudentSerialilzer

# Create your views here.


def student_api(request):
    if request.method == "GET":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get("id", None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerialilzer(stu)
            return JsonResponse(
                serializer.data, content_type="application/json", safe=False
            )
        stu = Student.objects.all()
        serializer = StudentSerialilzer(stu, many=True)
        return JsonResponse(
            serializer.data, content_type="application/json", safe=False
        )
    #creating an data point . 
    if (request.method=='POST'):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=StudentSerialilzer(data=pythondata,many=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'data has been created'}
            return JsonResponse(res,content_type='application/json',safe=False)
    return JsonResponse(serializer.errors,content_type='application/json',safe=False)
    
def update_items(request, pk):
    item = Student.objects.get(pk=pk)
    data = StudentSerialilzer(instance=item, data=request.data)
 
    if data.is_valid():
        data.save()
        return JsonResponse(data.data,safe=False)
    else:
        return JsonResponse(data.errors,safe=False)
    
def delete_items(request, pk):
    item = Student.objects.get(id=pk)
    item.delete()
    return JsonResponse({'msg':'success'},safe=False)