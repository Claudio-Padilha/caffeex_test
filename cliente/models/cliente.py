from django.db import models
from carro.models.carro import Carro


class Cliente(models.Model):
    nome = models.CharField(max_length=35)
    telefone = models.CharField(max_length=15)
    user = models.ForeignKey('user.User', related_name='client', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome}"

    @property
    def has_car(self):
        carros = Carro.objects.all().filter(cliente_id=self.id)
        if carros:
            return True
        else:
            return None
