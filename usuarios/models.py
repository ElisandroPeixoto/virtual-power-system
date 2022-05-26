from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Gerenciador de Usuarios Customizado
class UsuarioManager(BaseUserManager):

    use_in_migrations = True  # Permite salvar o usuário no BD

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('E-mail obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True')

        return self._create_user(email, password, **extra_fields)


class CustomUsuario(AbstractUser):
    email = models.EmailField('Email', unique=True)
    pais = models.CharField('Pais', max_length=50)
    estado = models.CharField('Estado', max_length=50)
    cidade = models.CharField('Cidade', max_length=50)

    is_staff = models.BooleanField('Membro da Equipe', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'pais', 'estado', 'cidade']

    objects = UsuarioManager()

    def __str__(self):
        return self.email
