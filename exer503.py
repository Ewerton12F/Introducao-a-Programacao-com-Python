# Exercício 5.3 Faça um programa para escrever a contagem regressiva do 
# lançamento de um foguete. O programa deve imprimir 10, 9, 8, ... , 1, 0 e Fogo! 
# na tela.

x=10
y=10+1
while y >= 0:
  x=y-1
  y-=1
  while x >= 0:
    print(x, end=" ") 
    x-=1
  print("") 
print("Fogo!")