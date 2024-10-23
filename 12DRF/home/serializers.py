from rest_framework import serializers
from .models import Person,Color


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Color
        fields=['color_name']


class PeopleSerializer(serializers.ModelSerializer):
    color=ColorSerializer()
    color_info=serializers.SerializerMethodField()
    class Meta:
        model=Person
        exclude=[] 
        # depth=1  # for priting all the fields under the color foreign key. 
        fields='__all__'

    # def validate(self,data):
    #         if data['age']<18:
    #             raise serializers.ValidationError('Age should greater than 18')
    #         return data


    def validate_age(self,age): #age should be greater than 18 logic.  
        if age<18:
            raise serializers.ValidationError("Age should be greather than 18 in order to register as a person")
        return age
    
    def validate_name(self,name): #implementing name shouldn't have special characters in them
        special_characters="!@#$%^&*()_+-=,./'"
        if any (c in special_characters for c in name):
            raise serializers.ValidationError('name cannot contain special characters')
        return name
    def get_color_info(self,obj):
        color_obj=Color.objects.get(id=obj.color.id)
        return {'color_name':color_obj.color_name,'hex_code':'#000'}
       