from django.urls import path, include
from rest_framework import routers
from citas import views

router = routers.DefaultRouter()
router.register(r'cita', views.CitaView, 'citas')

urlpatterns = [
    path("api/", include(router.urls))
]
