from rest_framework import serializers

from cliente.models.cliente import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone', 'user']


class CreateClienteSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    password = serializers.CharField()
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone', 'email', 'password']