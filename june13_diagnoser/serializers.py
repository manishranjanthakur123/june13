from rest_framework import serializers
from .models import MedicalEntity


class MedicalEntitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MedicalEntity
        fields = ('title','image')