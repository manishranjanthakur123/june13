from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from .views import MedicalEntityViewSet


router = routers.DefaultRouter()
router.register('medicalentity', MedicalEntityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]