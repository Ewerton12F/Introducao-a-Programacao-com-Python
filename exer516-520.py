# Exercício 5.16 Execute o Programa 5.1 para os seguintes valores:
# 501, 745, 384, 2, 7 e 1.

# Exercício 5.17 O que acontece se digitarmos 0 (zero) no valor a pagar?

# Exercício 5.18 Modifique o programa para também trabalhar com notas de R$100.

# Exercício 5.19 Modifique o programa para aceitar valores decimais, ou seja, 
# também contar moedas de 0,01, 0,02, 0,05, 0,10 e 0,50.

# Exercício 5.20 O que acontece se digitarmos 0,001 no programa anterior? 
# Caso ele não funcione, altere-o de forma a corrigir o problema.

# Programa 5.1 - Contagem de células / Exercícios 5.16 à 5.20

valor = float(input('Digite o valor a pagar: '))
cedulas = 0.0
atual = 100
apagar = valor

while True:
  if atual <= apagar:
    apagar -= atual
    cedulas += 1
  
  else:
    print(f'{cedulas} cédula(s) de R${atual:.2f}')
    if apagar == 0:
      break
    if atual == 100:
      atual = 50
    elif atual == 50:
      atual = 20
    elif atual == 20:
      atual = 10
    elif atual == 10:
      atual = 5
    elif atual == 5:
      atual = 1
    elif atual == 1:
      atual = 0.50
    elif atual == 0.50:
      atual = 0.25
    elif atual == 0.25:
      atual = 0.10
    elif atual == 0.10:
      atual = 0.05
    elif atual == 0.05:
      atual = 0.01
    cedulas = 0