
from typing import List

from src.model.fee_bank import FeeBank
from src.model.transaction import Transaction, TransactionType


class AccountBank:

    def __init__(self, transactions: List[Transaction], brokerage_balance: float, number_of_withdraws: int):
        self._transactions = transactions
        self._number_of_withdraws = number_of_withdraws
        self.total_withdraw = self.__total_withdraw
        self.total_deposit = self.__total_deposit
        self.brokerage_balance = brokerage_balance

    def profit(self, vai_sacar=True):
        return self.__profit_if_withdraw if vai_sacar else self.__profit_if_not_withdraw

    @property
    def __profit_if_withdraw(self) -> float:
        return self.__yield_in_case_of_withdraw - self.total_deposit

    @property
    def __profit_if_not_withdraw(self) -> float:
        return self.__yield_if_not_withdraw - self.total_deposit

    @property
    def __yield_in_case_of_withdraw(self):
        return self.__brokerage_balance_with_fee - (self.__cost_of_all_withdraws + FeeBank.WITHDRAW) + self.total_withdraw

    @property
    def __yield_if_not_withdraw(self):
        return self.brokerage_balance - self.__cost_of_all_withdraws + self.total_withdraw

    @property
    def __total_deposit(self):
        return self.__sum_by_type(TransactionType.DEPOSIT)

    @property
    def __total_withdraw(self):
        return self.__sum_by_type(TransactionType.WITHDRAW)

    @property
    def __brokerage_balance_with_fee(self):
        return (1 - FeeBank.BALANCE) * self.brokerage_balance

    @property
    def __cost_of_all_withdraws(self) -> float:
        return FeeBank.WITHDRAW * self._number_of_withdraws

    def __sum_by_type(self, transaction_type: TransactionType) -> float:
        transactions = list(filter(lambda transaction: transaction.type == transaction_type, self._transactions))
        sum_transactions = 0
        for transaction in transactions:
            sum_transactions += transaction.value
        return sum_transactions
