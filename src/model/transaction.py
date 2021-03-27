from datetime import datetime
from enum import Enum


class TransactionType(Enum):
    DEPOSIT = 1
    WITHDRAW = -1


class Transaction:
    def __init__(self, value: float, date: datetime, transacion_type: TransactionType):
        self.value = value
        self.date = date
        self.type = transacion_type

    def _real_value(self):
        return self.value * (1 if self.type == TransactionType.DEPOSIT else -1)

    def __str__(self):
        return str(self.__repr__())

    def __repr__(self):
        return self._real_value
