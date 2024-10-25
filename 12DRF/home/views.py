from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets,status
from .models import Person
from home.serializers import PeopleSerializer
from django.shortcuts import get_object_or_404

@api_view(["GET", "POST", "PATCH", "PUT", "DELETE"])
def peoples(request,id=None):
    if request.method == "GET":
        if id is not None:
            objs = Person.objects.filter(id=id)
            serializer = PeopleSerializer(objs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        objs=Person.objects.all()
        serializer = PeopleSerializer(objs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
   
    elif request.method == "POST":
        data = request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    elif request.method == "PUT":  # full update(replace) / create a new entry.
        data = request.data

        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    elif request.method == "PATCH":  # partial update
        data = request.data
        obj = Person.objects.get(id=data.get("id"))
        serializer = PeopleSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    elif request.method=='DELETE':
           # Check if ID is passed
        if id is not None:
            # Get the person by ID
            obj = get_object_or_404(Person, pk=id)
            obj.delete()
            return Response({'message': 'Person deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'ID not provided'}, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)




class PersonViewSet(viewsets.ModelViewSet):
    queryset=Person.objects.all
    serializer_class=PeopleSerializer

    def get_queryset(self,id=None):
        return Person.objects.all()  # Ensure it's returning a queryset, not a method or something else
    
    def reterive(self,request,*args,**kwargs):
        instance=self.get_object()
        serializer=self.get_serializer(instance)
        return Response(serializer.data)\
     # Optionally, override the destroy method if you want custom logic
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()  # Get the object to delete
        self.perform_destroy(instance)  # Perform the delete operation
        return Response(status=204)  # Return a No Content response
    
