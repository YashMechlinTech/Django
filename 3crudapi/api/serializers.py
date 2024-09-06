from rest_framework import serializers


from .models import Student


class StudentSerialilzer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['name','roll','city']


        #now we can skip the creating the create update methods
