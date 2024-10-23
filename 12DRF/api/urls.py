from home.views import peoples
from django.urls import path

urlpatterns = [
    path('peoples/',peoples),
    path('peoples/<int:id>',peoples,name="people_details")
]
