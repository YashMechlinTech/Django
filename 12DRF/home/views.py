from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
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
