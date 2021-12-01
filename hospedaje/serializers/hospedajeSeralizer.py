from django.db.models import fields
from rest_framework import serializers

from hospedaje.models import Hospedaje

class HospedajeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Hospedaje
        fields= '__all__'

