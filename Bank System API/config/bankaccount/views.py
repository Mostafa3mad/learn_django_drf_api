from django.shortcuts import render
from rest_framework import generics

from .models import BankAccount, Transaction
from .serializers import BankAccountSerializer, TransactionSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .services import MangeBankAccount ,MangeTransaction

class BankAccountListView(generics.ListCreateAPIView):
    queryset = MangeBankAccount.get_all_bank_accounts()
    serializer_class = BankAccountSerializer
BankAccount_view = BankAccountListView.as_view()


class TransactionCreateListView(generics.ListCreateAPIView):
    queryset = MangeTransaction.get_all_bank_transactions()
    serializer_class = TransactionSerializer
Transection_view = TransactionCreateListView.as_view()