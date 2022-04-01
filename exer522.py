# Exercício 5.22 Escreva um programa que exiba uma lista de opções (menu):
# adição,subtração, divisão, multiplicação e sair. Imprima a tabuada da 
# operação escolhida. Repita até que a opção saída seja escolhida.

print(f"\033[1;1;1m{'-' * 17}\033[0;0;0m")
print(f"\033[1;1;1m{'OPÇÕES':^17}\033[0;0;0m")
print(f"\033[1;1;1m{'-' * 17}\033[0;0;0m")

print(f"\033[1;31;3m{'1 - ADIÇÃO'}\033[0;0;0m")
print(f"\033[1;32;3m{'2 - SUBTRAÇÃO'}\033[0;0;0m")
print(f"\033[1;33;3m{'3 - DIVISÃO'}\033[0;0;0m")
print(f"\033[1;34;3m{'4 - MULTIPLICAÇÃO'}\033[0;0;0m")
print(f"\033[1;39;3m{'0 - SAIR'}\033[0;0;0m")

while True:
  print()
  opcao = int(input('Informe a opção desejada: '))
  print()
  x = 1
  if opcao == 1:
    print(f'\033[1;31;3mA tabuada de ADIÇÃO é:\033[0;0;0m')
    while x <= 10:
      y = 1
      print()
      print(f'\033[1;31;3mTabuada de {x}\033[0;0;0m')
      while y <= 10:
        print(f'\033[1;31;3m{x:2.0f} + {y:2.0f} = {x + y:2.0f}\033[0;0;0m')
        y += 1
      x += 1

  elif opcao == 2:
    print(f'\033[1;32;3mA tabuada de SUBTRAÇÃO é:\033[0;0;0m')
    while x <= 10:
      y = 1
      print()
      print(f'\033[1;32;3mTabuada de {x}\033[0;0;0m')
      while y <= 10:
        print(f'\033[1;32;3m{x:2.0f} - {y:2.0f} = {x - y:2.0f}\033[0;0;0m')
        y += 1
      x += 1

  elif opcao == 3:
    print(f'\033[1;33;3mA tabuada de DIVISÃO é:\033[0;0;0m')
    while x <= 10:
      y = 1
      print()
      print(f'\033[1;33;3mTabuada de {x}\033[0;0;0m')
      while y <= 10:
        print(f'\033[1;33;3m{x:2.0f} / {y:2.0f} = {x / y:2.3f}\033[0;0;0m')
        y += 1
      x += 1

  elif opcao == 4:
    print(f'\033[1;34;3mA tabuada de MULTIPLICAÇÃO é:\033[0;0;0m')
    while x <= 10:
      y = 1
      print()
      print(f'\033[1;34;3mTabuada de {x}\033[0;0;0m')
      while y <= 10:
        print(f'\033[1;34;3m{x:2.0f} * {y:2.0f} = {x * y:2.0f}\033[0;0;0m')
        y += 1
      x += 1

  elif opcao == 0:
    print(f'\033[3;39;45mSAIR!\033[0;0;0m')
    break

  else:
    print(f'\033[3;31;47m{" OPÇÃO INVÁLIDA! ":↔^30}\033[0;0;0m')