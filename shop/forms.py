from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image']
        labels = {
            'name': 'Название товара',
            'price': 'Цена товара',
            'description': 'Описание товара',
            'image': 'Фото'
        }
