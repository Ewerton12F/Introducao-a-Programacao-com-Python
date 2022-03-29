# Exercício 5.11 Escreva um programa que pergunte o depósito inicial e a taxa de
# juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses. 
# Escreva o total ganho com juros no período.

deposito = float(input('Informe o depósito inicial: '))
juros = float(input('Infome a taxa de juros: '))
totDep = 0
totJur = 0
x = 1

while x <= 24:
  total = deposito + (deposito * (juros / 100))
  totJur += total
  totDep += deposito
  print(f'O total do {x}º mês é: R${totJur:.2f}')
  if x == 24:
    print('-=' * 24)
    print(f'O total ganho com juros no período foi R${totJur - totDep:.2f}')
  x += 1