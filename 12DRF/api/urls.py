from home.views import peoples
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from home.views import PersonViewSet

router = DefaultRouter()
router.register(r'person_viewset_data', PersonViewSet, basename="person_viewset_data")


urlpatterns = [
       path("", include(router.urls)),
    path("peoples/", peoples),
    path("peoples/<int:id>", peoples, name="people_details"),
 
]
