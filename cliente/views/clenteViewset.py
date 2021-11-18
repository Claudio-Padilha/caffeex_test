from django.forms.models import model_to_dict
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from cliente.models.cliente import Cliente
from cliente.serializers.clienteSerializer import ClienteSerializer, CreateClienteSerializer
from user.models.user import User


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateClienteSerializer
        else:
            return ClienteSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        else:
            return [permissions.IsAuthenticated()]

    def create(self, request):
        user = User.objects.create_user(email=request.data['email'], password=request.data['password'])
        cliente = Cliente.objects.create(nome=request.data['nome'], telefone=request.data['telefone'], user=user)
        return Response(model_to_dict(cliente))
