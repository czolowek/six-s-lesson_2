from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название товара')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    description = models.TextField(verbose_name='Описание', blank=True)
    image = models.ImageField(upload_to='products/', verbose_name='Фото')

    def __str__(self):
        return self.name
