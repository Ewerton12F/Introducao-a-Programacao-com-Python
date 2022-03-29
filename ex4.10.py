# Exercício 4.10 Escreva um programa que calcule o preço a pagar pelo 
# fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o 
# tipo de instalação: R para residências, I para indústrias e C para comércios. 
# Calcule o preço a pagar de acordo com a tabela a seguir.

# | Tipo        | Faixa (kWh)   | Preço   |
# | ----------- | ------------- | ------- |
# | Residencial | Até 500       | R$ 0,40 |
# |             | Acima de 500  | R$ 0,65 |
# | ------------------------------------- |
# | Comercial   | Até 1000      | R$ 0,55 |
# |             | Acima de 1000 | R$ 0,60 |
# | ------------------------------------- |
# | Industrial  | Até 5000      | R$ 0,55 |
# |             | Acima de 5000 | R$ 0,60 |

quant_kwh = float(input('Informe a quantidade de kWh consumida: '))
instalacao = str(input('Informe o tipo de instalação (R para residências, I para indústrias e C para comércios): '))

preco = 0

if instalacao == 'R':
  if quant_kwh <= 500:
    preco += 0.40
  else:
    preco += 0.65
elif instalacao == 'C':
  if quant_kwh <= 1000:
    preco += 0.55
  else:
    preco += 0.60
elif instalacao == 'I':
  if quant_kwh <= 5000:
    preco += 0.55
  else:
    preco += 0.60

print(f'O valor a pagar será R${quant_kwh * preco:6.2f}')