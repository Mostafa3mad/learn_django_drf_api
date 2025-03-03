# Generated by Django 5.1.6 on 2025-02-17 18:30

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankaccount', '0002_alter_bankaccount_account_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_number', models.CharField(blank=True, max_length=15, unique=True)),
                ('transaction_type', models.CharField(choices=[('DP', 'Deposit'), ('WD', 'Withdrawal')], max_length=2)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='bankaccount.bankaccount')),
            ],
            options={
                'db_table': 'transaction',
                'ordering': ['-created_at'],
            },
        ),
    ]
