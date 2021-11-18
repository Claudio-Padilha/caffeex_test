from django.db import models


class Carro(models.Model):
    modelo = models.CharField(max_length=20)
    ano = models.CharField(max_length=20)
    cor = models.CharField(max_length=20)
    placa = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    cliente = models.ForeignKey('cliente.Cliente', on_delete=models.CASCADE, null=True)
