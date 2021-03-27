# Mercado Bitcoin Profit Analyst
Código que levanta estatísticas sobre lucro (em reais) sob criptomoedas da corretora Mercado Bitcoin.

## Como usar

1) Acesse a plataforma do [Mercado Bitcoin](https://www.mercadobitcoin.com.br/)
2) Acesse seu extrato em reais
3) Selecione a opção "ver apenas movimentações em BRL - Reais"
4) Para cada ano, clique no ícone de download
5) Pegue os arquivos csv baixados e os renomei para `extrato<ano>.csv` (.csv é apenas a extensão do arquivo). Exemplo: `extrato_2020.csv`
6) Coloque os arquivos renomeados na pasta `data_files/extratos` (exclua os arquivos anteriores)
7) Coloque no arquivo `balance.txt` localizado na pasata `data_files` o valor que aparece no seu saldo da plataforma do [Mercado Bitcoin](https://www.mercadobitcoin.com.br/)
8) Execute o programa