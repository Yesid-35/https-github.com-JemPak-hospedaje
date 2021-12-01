from django.db import models

planes=(
        (1,'Planes Familiares'),
        (2,'Luna de Miel'),
        (3, 'Excursiones')
)

class Hospedaje (models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    ciudad = models.CharField("Ciudad", max_length=50, null=True)
    direccion = models.CharField("direccion", max_length=200, null=True, blank=False)
    personas = models.IntegerField("personas",null=True)
    tipo_hospedaje = models.CharField("Tipo de Hospedaje", max_length=50, choices = planes,blank=True, null=True)
    fecha_reserva = models.DateField("Fecha de reserva", auto_now_add=True)
    valor = models.BigIntegerField("Monto a pagar", null=True)