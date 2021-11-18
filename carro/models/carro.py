from django.db import models
from django.forms.models import model_to_dict


class Carro(models.Model):
    modelo = models.CharField(max_length=20)
    ano = models.CharField(max_length=20)
    cor = models.CharField(max_length=20)
    placa = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    cliente = models.ForeignKey('cliente.Cliente', on_delete=models.CASCADE, null=True)
