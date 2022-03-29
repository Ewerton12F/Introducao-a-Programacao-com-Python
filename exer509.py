# Exercício 5.9 Escreva um programa que leia dois números. Imprima a divisão 
# inteira do primeiro pelo segundo, assim como o resto da divisão. 
# Utilize apenas os operadores de soma e subtração para calcular o resultado. 
# Lembre-se de que podemos entender o quociente da divisão de dois números como 
# a quantidade de vezes que podemos retirar o divisor do dividendo. 
# Logo, 20 / 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20 

n1 = int(input('Informe o 1º número: '))
n2 = int(input('Informe o 2º número: '))
pn = n1
sn = n2
divInt = 0
resto = 0

while True:
  if n1 - n2 >= 0:
    divInt += 1
    if n1 > 0:
      resto = n1
    n1 -= n2
    resto = n1
    continue
  else:
    print(f'Resultado da divisão inteira de {pn} por {sn} é {divInt}')
    break

print(f'O resto da divisão é {resto}')