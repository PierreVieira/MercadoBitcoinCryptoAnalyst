from src.controller.account_bank_generator import BankGenerator
from src.controller.file_manager import FileManager

if __name__ == '__main__':
    brokerage_balance = FileManager.get_brokerage_balance()
    bank = BankGenerator.generate_bank(brokerage_balance)
    print(f'Total depositado: R$ {bank.total_deposit:.2f}')
    print(f'Total sacado: R$ {bank.total_withdraw:.2f}')
    print(f'Total em conta: R$ {bank.brokerage_balance:.2f}')
    print(f'Total sacado + em conta: R$ {(bank.total_withdraw + bank.brokerage_balance):.2f}\n')
    print(f'Lucro total se não sacar: R$ {bank.profit(vai_sacar=False):.2f}')
    print(f'Lucro total se sacar: R$ {bank.profit(vai_sacar=True):.2f}')
