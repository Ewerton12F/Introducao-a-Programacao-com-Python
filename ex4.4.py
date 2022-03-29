# Exercício 4.4 Escreva um programa que pergunte o salário do funcionário e 
# calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule 
# um aumento de 10%. Para os inferiores ou iguais, de 15%.

salario = float(input('Informe o salário: '))

if salario > 1250:
  sal_maior = salario + (salario * 0.1)
  print(f'O salário é maior que R$1.250,00. O novo salário será de R${sal_maior:6.2f}')
if salario < 1250:
  sal_menor = salario + (salario * 0.15)
  print(f'O salário é menor que R$1.250,00. O novo salário será de R${sal_menor:6.2f}')