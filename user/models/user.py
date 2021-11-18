from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class UserManager (BaseUserManager):
    def create_user(self, email, password, username=None):
        if not email:
            raise ValueError("Por favor, informe um email!")
        if not password:
            raise ValueError("Por favor, informe uma senha!")
        email = self.normalize_email(email)
        user = self.model(username=email, email=email, is_active=True)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, name, email, password, username=None):
        if not email:
            raise ValueError("Email não informado")
        if not password:
            raise ValueError("Senha não informada")
        email = self.normalize_email(email)
        user = self.model(username=email, email=email, is_active=True, is_staff=True, is_superuser=True)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User (AbstractUser):
    email = models.CharField(max_length=100,unique=True)          
    token = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    USER_CREATE_PASSWORD_RETYPE = True
    REQUIRED_FIELDS = []

    objects = UserManager()
