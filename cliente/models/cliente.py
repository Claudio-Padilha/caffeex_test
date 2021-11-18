from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=35)
    telefone = models.CharField(max_length=15)
    user = models.ForeignKey('user.User', related_name='client', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome}"
