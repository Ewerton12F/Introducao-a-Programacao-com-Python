# Exercício 4.8 Escreva um programa que leia dois números e que pergunte
# qual operação você deseja realizar. Você deve poder calcular 
# soma (+), subtração (-), multiplicação (*) e # divisão (/). 
# Exiba o resultado da operação solicitada.

numero_1 = int(input('Informe o primeiro número: '))
numero_2 = int(input('Informe o segundo número: '))
operacao = str(input('Informe a operação de sua escolha: '))

if operacao == 'positivo' or operacao == '+':
  resultado = numero_1 + numero_2
elif operacao == 'negativo':
  resultado = numero_1 - numero_2
elif operacao == 'multiplicação':
  resultado = numero_1 * numero_2
elif operacao == 'divisão':
  resultado = numero_1 / numero_2
else:
  print('Operação inválida!')

print(f'A operação escolhida foi "{operacao}" e o resultado do calculo entre os dois números é: {resultado}')