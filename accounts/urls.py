from django.urls import path
from .views import register_user, register_admin, UserLoginView, UserLogoutView

urlpatterns = [
    path('register/', register_user, name='register'),
    path('register_admin/', register_admin, name='register_admin'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
