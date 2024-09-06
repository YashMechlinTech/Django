from .serializers import *
from .models import Student
from .serializers import StudentSerialilzer
from rest_framework import viewsets
from rest_framework.authentication  import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerialilzer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]

