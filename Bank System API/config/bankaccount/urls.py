from django.urls import path
from django.conf.urls.static import static
from rest_framework import routers
from .views import BankAccount_view,Transection_view

app_name = 'bank_account'

urlpatterns = [
    path('bank-account/', BankAccount_view, name='created_list_bank_account'),
    path('transaction/',Transection_view,name='created_list_transaction'),

]