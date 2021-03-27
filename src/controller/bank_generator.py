from datetime import datetime

from src.controller.file_manager import FileManager
from src.model.bank import Bank
from src.model.transaction import Transaction, TransactionType


class BankGenerator:
    @staticmethod
    def generate_bank(brokerage_balance: float):
        operations = FileManager.get_csv_to_list()
        list_transactions = []
        for operation in operations:
            if operation['Categoria'] == 'Depósito' or operation['Categoria'] == 'Saque/Retirada':
                value = abs(float(operation['Quantidade']))
                date = BankGenerator.__get_date(operation['Data'])
                transaction_type = TransactionType.DEPOSIT if operation['Categoria'] == 'Depósito' else TransactionType.WITHDRAW
                list_transactions.append(Transaction(value, date, transaction_type))
        return Bank(list_transactions, brokerage_balance)

    @classmethod
    def __get_date(cls, date_string: str):
        days, time = date_string.split()
        year, month, day = map(int, days.split('-'))
        hour, minute, second = map(int, time.split(':'))
        date = datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
        return date
