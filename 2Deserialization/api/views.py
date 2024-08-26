from django.shortcuts import render
import io
from .serializers import StudentSerializer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_create(request):
    if request.method == "POST":
        try:
            json_data = request.body
            print("Step 1: request.body data saved into json_data", json_data)

            # Convert JSON byte data to stream
            stream_data = io.BytesIO(json_data)
            print("Step 2: JSON data is converted into a stream of bytes")

            # Parse stream data to Python dictionary
            python_data = JSONParser().parse(stream_data)
            print("Step 3: Stream data is converted into python_data")

            # Initialize the serializer with the parsed data
            serializer = StudentSerializer(data=python_data)

            # Validate and save the data
            if serializer.is_valid():
                serializer.save()  # Save data to the database
                res = {"msg": "Data created successfully"}
                return JsonResponse(res, safe=False)
            else:
                # Handle case where serializer data is invalid
                return JsonResponse(serializer.errors, safe=False, status=400)
        except Exception as e:
            print(f"Error: {e}")
            res = {"msg": "Internal Server Error"}
            return JsonResponse(res, safe=False, status=500)

    # If the request method is not POST, return a method not allowed error
    return JsonResponse({"msg": "Method not allowed"}, status=405)
