# Exercício 5.6 Altere o programa anterior para exibir os resultados no mesmo 
# formato de uma tabuada: 2 x 1 = 2, 2 x 2 = 4, ...

n = int(input('Tabuada de: '))
x = 1
while x <= 10:
  print(f'{x:2.0f} x {n} = {n * x}')
  x = x + 1