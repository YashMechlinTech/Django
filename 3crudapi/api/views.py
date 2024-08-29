from django.http import JsonResponse
import io
from rest_framework.parsers import JSONParser
from .serializers import *
from .models import Student
from .serializers import StudentSerialilzer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response

# Create your views here.


@csrf_exempt
def student_api(request):
    if request.method == "GET":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get("id", None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerialilzer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()  # if we dont want any id .
        serializer = StudentSerialilzer(stu, many=True)
        return Response(serializer.data)
    # creating an data point .

    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerialilzer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data has been added to the table"}, status=200)
        return Response(serializer.errors, status=400)
    return Response(
        {"msg": "An error occured nor get request nor post request accepted. "},
        status=400,
    )
