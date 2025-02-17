from rest_framework import serializers
from .models import BankAccount,Transaction
from .services import MangeBankAccount

class BankAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankAccount
        fields = '__all__'
        read_only_fields = ['account_number','account_number','is_active']
    def create(self, validated_data):

        return MangeBankAccount.create_bank_account(**validated_data)

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields = ["transaction_number","created_at"]

