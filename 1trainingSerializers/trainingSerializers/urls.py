

from django.contrib import admin
from django.urls import path
from API import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/<int:pk>',views.student_detail),
    path('stuinfo/',views.student_list)
]


#instead of using the json_data conversion and http response just use the JSONResponse 