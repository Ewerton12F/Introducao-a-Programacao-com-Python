# Exercício 5.7 Modifique o programa anterior de forma que o usuário também 
# digite o início e o fim da tabuada, em vez de começar com 1 e 10.

n = int(input('Tabuada de: '))
i = int(input('Informe o início da tabuada: '))
f = int(input('Informe o fim da tabuada: '))
x = i

while x >= i and x <= f:
  print(f'{x:2.0f} x {n} = {n * x}')
  x = x + 1