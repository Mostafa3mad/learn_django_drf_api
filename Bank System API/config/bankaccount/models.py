from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from .utils import Helper

# Create your models here.
class BankAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bank_account')
    account_number = models.CharField(max_length=15,unique=True,blank=True)
    balance = models.DecimalField(decimal_places=2, max_digits=10,default=0.0,validators=[MinValueValidator(0.00)])
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        db_table = 'bank_account'
        constraints = [
            models.CheckConstraint(
                check=models.Q(balance__gt=0),
                name='balance_greater_than_zero'
            )
        ]
        indexes = [
            models.Index(
                fields=['balance'],
            )
        ]

    def __str__(self):
        return f'{str(self.user.username)} - {self.account_number}'
    def save(self, *args, **kwargs):
        if not self.account_number:
            self.account_number = Helper.genrate_accunt_number(prefix='EG')
        super().save(*args, **kwargs)


class Transaction(models.Model):
    class TransactionType(models.TextChoices):
        Deposit = 'DP' , 'Deposit'
        WITHDRAWAL = 'WD' , 'Withdrawal'

    transaction_number = models.CharField(max_length=15,unique=True,blank=True)
    transaction_type = models.CharField(max_length=2,choices=TransactionType)
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE,related_name='transactions')
    amount = models.DecimalField(max_digits=10,decimal_places=2,default=0,validators=[MinValueValidator(0.00)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{str(self.transaction_type)} - {self.amount} - {self.account.account_number}'

    def clean(self):
        if (self.transaction_type in ['Withdrawal'] and self.account.balance < self.amount):
            raise ValidationError('Not enough balance')

        return super().clean()

    def save(self, *args, **kwargs):
        self.clean()
        if not self.transaction_number:
            self.transaction_number  = Helper.genrate_transaction_number()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'transaction'
        ordering = ['-created_at']
