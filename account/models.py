from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail
from django.db import models


class UserManager(BaseUserManager):
    def _create(self, username, password, **extra_fields):

        if not username:
            raise ValueError('Username is required!')
        # email = self.normalize_email(email)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, password, **extra_fields):
        extra_fields.setdefault('is_active', False)
        extra_fields.setdefault('is_staff', False)
        return self._create(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        return self._create(username, password, **extra_fields)


class User(AbstractBaseUser):
    # email = models.EmailField(primary_key=True)
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    def has_module_perms(self, app_label):
        return self.is_staff

    def has_perm(self, obj=None):
        return self.is_staff

    # def generate_activation_code(self):
    #     from django.utils.crypto import get_random_string
    #
    #     code = get_random_string(8)
    #     self.activation_code = code
    #     self.save()
    #     return code
    #
    # @staticmethod
    # def send_activation_mail(email, code):
    #     message = f'Ваш код активации: {code}'
    #     send_mail('Активация аккаунта',
    #               message, 'matraimov.daniel@gmail.com',
    #               [email])