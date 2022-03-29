# Exercício 5.12 Altere o programa anterior de forma a perguntar também o valor 
# depositado mensalmente. Esse valor será depositado no início de cada mês, e 
# você deve considerá-lo para o cálculo de juros do mês seguinte.

deposito = float(input('Informe o depósito inicial: '))
juros = float(input('Infome a taxa de juros: '))
depMes = 0
totJur = 0
totSeg = 0
x = 1

while x <= 24:
  total = (deposito + (deposito * (juros / 100))) + (depMes + (depMes * (juros / 100)))
  totJur += total
  depMes = float(input(f'Informe o valor depositado no {x}º mês: R$'))
  print(f'O total do {x}º mês é: R${totJur + depMes:.2f}.')
  x += 1