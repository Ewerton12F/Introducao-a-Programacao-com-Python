# Exercício 5.5 Reescreva o programa anterior para escrever os 10 primeiros
# múltiplos de 3.

x = 1
while x in range(10):
  if x % 3 == 0:
    print(x)
  x = x + 1