# Exercício 5.14 Escreva um programa que leia números inteiros do teclado. 
# O programa deve ler os números até que o usuário digite 0 (zero). l o final da
# execução, exiba a quantidade de números digitados, assim como a soma e a média
# aritmética.

x = 0
s = 0

while True:
  num = int(input('Digite um número a somar ou 0 para sair: '))
  if num == 0:
    print('Você saiu!')
    print(f'A quantidade de números digitados foi {x} e a média aritimética é {s / x}.')
    break
  s += num
  x += 1