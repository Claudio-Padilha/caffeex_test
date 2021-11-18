from http import client
from django.test import TestCase

from carro.models.carro import Carro
from cliente.models.cliente import Cliente
from user.models.user import User


class CarroTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(email="teste@email.com", password="111111")
        cliente = Cliente.objects.create(nome="cliente teste", telefone="000000000", user=user)
        print(cliente)
        Carro.objects.create(modelo="aaa", ano="1999", cor="prata", placa="QQQ2222", cliente=cliente)

    def test_user_has_car(self):
        cliente = Cliente.objects.get(nome="cliente teste")
        self.assertEqual(cliente.has_car, True)
