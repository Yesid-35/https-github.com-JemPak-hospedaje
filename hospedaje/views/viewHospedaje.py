from rest_framework import generics
from hospedaje.models import Hospedaje
from hospedaje.serializers import HospedajeSerializer

class hospedajeDetails(generics.ListCreateAPIView):
    queryset = Hospedaje.objects.all()
    serializer_class = HospedajeSerializer

class hospedajeRetrieveUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hospedaje.objects.all()
    serializer_class = HospedajeSerializer

class filterByTypeHospedaje(generics.ListAPIView):
    serializer_class = HospedajeSerializer
    def get_queryset(self):
        queryset = Hospedaje.objects.filter(tipo_hospedaje = self.kwargs["type"])
        return queryset

class filterBycity(generics.ListAPIView):
    serializer_class = HospedajeSerializer
    def get_queryset(self):
        queryset = Hospedaje.objects.filter(ciudad = self.kwargs["city"])
        return queryset

