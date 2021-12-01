# Generated by Django 3.2.7 on 2021-12-01 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospedaje',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ciudad', models.CharField(max_length=50, null=True, verbose_name='Ciudad')),
                ('direccion', models.CharField(max_length=200, null=True, verbose_name='direccion')),
                ('personas', models.IntegerField(null=True, verbose_name='personas')),
                ('tipo_hospedaje', models.CharField(blank=True, choices=[(1, 'Planes Familiares'), (2, 'Luna de Miel'), (3, 'Excursiones')], max_length=50, null=True, verbose_name='Tipo de Hospedaje')),
                ('fecha_reserva', models.DateField(auto_now_add=True, verbose_name='Fecha de reserva')),
                ('valor', models.BigIntegerField(null=True, verbose_name='Monto a pagar')),
            ],
        ),
    ]
