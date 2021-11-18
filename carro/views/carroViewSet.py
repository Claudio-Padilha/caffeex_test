from django.forms.models import model_to_dict
from rest_framework import permissions, viewsets
from rest_framework.response import Response

from carro.models.carro import Carro
from carro.serializers.carroSerializer import CarroSerializer


def get_car_if_permited(client_id, car_id):
    try:
        car = Carro.objects.get(pk=car_id)
    except Carro.DoesNotExist:
        raise ValueError("Carro não cadastrado")
    if car.cliente.id == client_id:
        if not car.is_active:
            raise ValueError("Carro já foi apagado")
        return car
    return None
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
        car = get_car_if_permited(request.user.client.all().first().id, kwargs['pk'])
        if car:
            car.is_active = False
            car.save()
            return Response(status=204)
        raise ValueError("Carro de outro proprietário")

    def list(self, request):
        return Response([model_to_dict(car) for car in Carro.objects.all().filter(
            cliente_id=request.user.client.all().first().id, is_active=True)])

    def retrieve(self, request, *args, **kwargs):
        car = get_car_if_permited(request.user.client.all().first().id, kwargs['pk'])
        if car:
            ret = model_to_dict(car)
            del ret['cliente']
            del ret['is_active']
            return Response(ret)
        raise ValueError("Carro de outro proprietário")
    
    def update(self, request, *args, **kwargs):
        car = get_car_if_permited(request.user.client.all().first().id, kwargs['pk'])
        print(car)
        if car:
            car.modelo = request.data['modelo']
            car.ano = request.data['ano']
            car.cor = request.data['cor']
            car.placa = request.data['placa']
            car.save()
            return Response({"Atualizado": car.id})
        raise ValueError("Carro de outro proprietário")

    def partial_update(self, request, *args, **kwargs):
        car = get_car_if_permited(request.user.client.all().first().id, kwargs['pk'])
        if car:
            if 'modelo' in request.data:
                car.modelo = request.data['modelo']
            if 'ano' in request.data:
                car.ano = request.data['ano']
            if 'cor' in request.data:
                car.cor = request.data['cor']
            if 'placa' in request.data:
                car.placa = request.data['placa']
            car.save()
            return Response({"Atualizado": car.id})
        raise ValueError("Carro de outro proprietário")
