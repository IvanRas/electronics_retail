from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    first_name = models.CharField(max_length=150, verbose_name='имя', blank=True)
    last_name = models.CharField(max_length=150, verbose_name='фамилия', blank=True)
    surname = models.CharField(max_length=150, verbose_name='отчество',  blank=True)
    email = models.EmailField(unique=True, verbose_name='email')

    def __str__(self):
        return f' {self.first_name} {self.last_name} {self.surname} {self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
