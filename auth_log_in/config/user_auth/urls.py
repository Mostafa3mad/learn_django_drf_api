from django.urls import path
from .views import RegiserUser_view

app_name = 'user_auth'

urlpatterns = [
    path('Regiser/', RegiserUser_view, name='Regiser'),
]