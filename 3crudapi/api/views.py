from .models import Student
from .serializers import StudentSerialilzer
from rest_framework import viewsets
# Create your views here.


class StudentModelViewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerialilzer


