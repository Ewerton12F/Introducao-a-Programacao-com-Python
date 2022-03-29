# Exercício 4.3 Escreva um programa que leia três números e que imprima o maior
# e o menor.

n1 = int(input('Informe o 1º número: '))
n2 = int(input('Informe o 2º número: '))
n3 = int(input('Informe o 3º número: '))

if n1 > n2:
  maior = n1
if n1 > n3:
  maior = n1

if n2 > n1:
  maior = n2
if n2 > n3:
  maior = n2
  
if n3 > n1:
  maior = n3
if n3 > n2:
  maior = n3

#

if n1 < n2:
  menor = n1
if n1 < n3:
  menor = n1

if n2 < n1:
  menor = n2
if n2 < n3:
  menor = n2
  
if n3 < n1:
  menor = n3
if n3 < n2:
  menor = n3

print(f'O número {maior} é o maior e o número {menor} é o menor.')