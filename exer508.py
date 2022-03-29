# Exercício 5.8 Escreva um programa que leia dois números. Imprima o resultado 
# da multiplicação do primeiro pelo segundo. Utilize apenas os operadores de 
# soma e subtração para calcular o resultado. Lembre-se de que podemos entender 
# a multiplicação de dois números como somas sucessivas de um deles. 
# Assim, 4 x 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.

n1 = int(input('Informe o 1º número: '))
n2 = int(input('Informe o 2º número: '))
temp = 0
result = 0

while n2 >= 1:
  temp += n1
  n2 -= 1

print(f'O resultado da multiplicação é {temp}.')