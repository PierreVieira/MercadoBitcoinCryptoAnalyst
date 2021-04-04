from datetime import datetime

from src.controller.file_manager import FileManager
from src.model.account_bank import AccountBank
from src.model.transaction import Transaction, TransactionType


class BankGenerator:
    @staticmethod
    def generate_bank(brokerage_balance: float):
        operations = FileManager.get_csv_to_list()
        list_transactions = []
        number_of_withdraws = 0
        for operation in operations:
            if operation['Categoria'] == 'Depósito' or operation['Categoria'] == 'Saque/Retirada':
                if operation['Categoria'] == 'Saque/Retirada':
                    number_of_withdraws += 1
                value = abs(float(operation['Quantidade']))
                date = BankGenerator.__get_date(operation['Data'])
                transaction_type = TransactionType.DEPOSIT if operation['Categoria'] == 'Depósito' else TransactionType.WITHDRAW
                list_transactions.append(Transaction(value, date, transaction_type))
        return AccountBank(list_transactions, brokerage_balance, number_of_withdraws)

    @classmethod
    def __get_date(cls, date_string: str):
        days, time = date_string.split()
        year, month, day = map(int, days.split('-'))
        hour, minute, second = map(int, time.split(':'))
        date = datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
        return date
