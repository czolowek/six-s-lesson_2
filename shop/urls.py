from django.urls import path
from .views import home, admin_page

urlpatterns = [
    path('', home, name='home'),
    path('admin_page/', admin_page, name='admin_page'),
]
