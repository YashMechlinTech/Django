from django.db import models

class Color(models.Model):
    color_name=models.CharField(max_length=100,)

    def __str__(self) -> str:
        return self.color_name


# Create your models here.
class Person(models.Model):
    color=models.ForeignKey(Color,models.CASCADE,related_name="color",null=True,blank=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    
    
