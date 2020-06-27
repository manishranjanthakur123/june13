from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import MedicalEntity
from .serializers import MedicalEntitySerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from june13_auth.backends import JWTAuthentication


# Create your views here.
class MedicalEntityViewSet(viewsets.ModelViewSet):
    queryset = MedicalEntity.objects.all()
    serializer_class = MedicalEntitySerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        image = request.data['image']
        title = request.data['title']
        try:
            MedicalEntity.objects.create(title=title, image=image)
        except:
            return Response({'response': 'error'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'response':'Uploaded Successfully'}, status=status.HTTP_201_CREATED)