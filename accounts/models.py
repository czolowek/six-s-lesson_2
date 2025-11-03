from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    city = models.CharField(max_length=100, verbose_name='Город', blank=True)
    is_admin_user = models.BooleanField(default=False, verbose_name='Является администратором')

    def __str__(self):
        return self.username
