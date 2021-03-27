from src.controller.bank_generator import BankGenerator
from src.controller.file_manager import FileManager

if __name__ == '__main__':
    brokerage_balance = FileManager.get_brokerage_balance()
    bank = BankGenerator.generate_bank(brokerage_balance)
    print(f'Total depositado: R$ {bank.total_deposit:.2f}')
    print(f'Total sacado: R$ {bank.total_withdraw:.2f}\n')
    print(f'Lucro total se não sacar incluindo valor já sacado: R$ {bank.profit(incluir_valor_ja_sacado=True, vai_sacar=False):.2f}')
    print(f'Lucro total em caso de saque incluindo valor já sacado: R$ {bank.profit(incluir_valor_ja_sacado=True, vai_sacar=True):.2f}')
    print(f'Lucro total se não sacar não incluindo valor já sacado: R$ {bank.profit(incluir_valor_ja_sacado=False, vai_sacar=False):.2f}')
    print(f'Lucro total se sacar não inculindo valor já sacado: R$ {bank.profit(incluir_valor_ja_sacado=False, vai_sacar=True):.2f}')
