import json

from django.forms.models import model_to_dict
from django.contrib.auth import login
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from user.models.user import User


class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        pwd_valid = False
        body = json.loads(request.body)
        custom_response = {}
        user = None
        try:
            user = User.objects.get(email=body['email'])
        except:
            return Response("Usuário inválido", status=500)
        pwd_valid = check_password(body['password'], user.password)
        if pwd_valid:
            token, _ = Token.objects.get_or_create(user=user)
            custom_response = {"user": model_to_dict(user), "token": token.key}
            login(request, user)
        else: 
            custom_response = {"status": "erro", "mensagem": "Senha inválida!"}
            return Response(custom_response, status=500)
        return Response(custom_response)
