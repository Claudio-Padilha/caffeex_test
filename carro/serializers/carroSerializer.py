# rest framework
from rest_framework import serializers

# our apps
from carro.models.carro import Carro


class CarroSerializer(serializers.ModelSerializer):
    class Meta:
      model = Carro
      fields = ['modelo', 'ano', 'cor', 'placa']
