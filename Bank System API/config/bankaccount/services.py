from .models import BankAccount ,Transaction



class MangeBankAccount:
    @staticmethod
    def get_account_by_id(pk):
        return BankAccount.objects.get(id=pk)
    @staticmethod
    def create_bank_account(**user):
        bank_account = BankAccount.objects.create(
            **user
        )
        return bank_account
    @staticmethod
    def get_all_bank_accounts():
        return BankAccount.objects.all()

class MangeTransaction:
    @staticmethod
    def get_transaction_by_id(pk):
        return Transaction.objects.get(id=pk)

    @staticmethod
    def get_all_bank_transactions():
        return Transaction.objects.select_related('account').all()
