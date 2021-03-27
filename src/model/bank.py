from typing import List

from src.model.transaction import Transaction, TransactionType


class Bank:
    def __init__(self, transactions: List[Transaction], brokerage_balance: float):
        self._transactions = transactions
        self._brokerage_balance = brokerage_balance

    @property
    def total_deposit(self):
        return self._sum_by_type(TransactionType.DEPOSIT)

    @property
    def total_withdraw(self):
        return self._sum_by_type(TransactionType.WITHDRAW)

    def profit(self, incluir_valor_ja_sacado=True, vai_sacar=True):
        brokerage_balance = self._brokerage_balance
        total_withdraw = self.total_withdraw
        total_deposit = self.total_deposit
        if vai_sacar and incluir_valor_ja_sacado:
            return brokerage_balance * 0.981 - 2.99 + total_withdraw - total_deposit
        elif not vai_sacar and incluir_valor_ja_sacado:
            return brokerage_balance + total_withdraw - total_deposit
        elif vai_sacar and not incluir_valor_ja_sacado:
            return brokerage_balance * 0.981 - 2.99 - total_deposit
        elif not vai_sacar and not incluir_valor_ja_sacado:
            return brokerage_balance - total_deposit
        raise TypeError('Impossible')

    @property
    def profit_if_withdraw(self):
        return 0.981 * self._brokerage_balance + self.total_withdraw - self.total_deposit

    def _sum_by_type(self, transaction_type: TransactionType) -> float:
        transactions = list(filter(lambda transaction: transaction.type == transaction_type, self._transactions))
        sum_transactions = 0
        for transaction in transactions:
            sum_transactions += transaction.value
        return sum_transactions
