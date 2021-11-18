from http import client
from django.forms.models import model_to_dict
from rest_framework import permissions, viewsets
from rest_framework.response import Response
import carro

from carro.models.carro import Carro
from carro.serializers.carroSerializer import CarroSerializer

class CarroViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer

    def create(self, request):
        car = Carro.objects.create(
            modelo = request.data['modelo'],
            ano = request.data['ano'],
            cor = request.data['cor'],
            placa = request.data['placa'],
            cliente = request.user.client.all().first()
        )
        ret = model_to_dict(car)
        del ret['cliente']
        return Response(ret)

    def destroy(self, request, *args, **kwargs):
        try:
            car = Carro.objects.get(pk=kwargs['pk'])
        except Carro.DoesNotExist:
            raise ValueError("Carro não cadastrado")
        
        if car.cliente.id == request.user.client.all().first().id:
            car.is_active = False
            car.save()
            return Response(status=204)
        raise ValueError("Carro de outro proprietário")

    def list(self, request):
        return Response([model_to_dict(car) for car in Carro.objects.all().filter(cliente_id=request.user.client.all().first().id, is_active=True)])

    def retrieve(self, request, *args, **kwargs):
        try:
            car = Carro.objects.get(pk=kwargs['pk'])
        except Carro.DoesNotExist:
            raise ValueError("Carro não cadastrado")
        if car.cliente.id == request.user.client.all().first().id:
            if not car.is_active:
                raise ValueError("Carro apagado")
            ret = model_to_dict(car)
            del ret['cliente']
            del ret['is_active']
            return Response(ret)
        raise ValueError("Carro de outro proprietário")
