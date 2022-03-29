# Exercício 4.9 Escreva um programa para aprovar o empréstimo bancário para 
# compra de uma casa. O programa deve perguntar o valor da casa a comprar, o 
# salário e a quantidade de anos a pagar. O valor da prestação mensal não pode 
# ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor
# da casa a comprar dividido pelo número de meses a pagar.

valor_casa = float(input('Informe o valor da casa: '))
salario = float(input('Informe o salário: '))
anos_pagar = int(input('Informe a quantidade de anos a pagar: '))

meses = anos_pagar * 12
parcela = valor_casa / meses

limite_sal = salario - (salario * 0.7)

if parcela <= limite_sal:
  print(f'O valor da parcela será R${parcela:5.2f}')
else:
  print('O valor da prestação não pode ser superior a 30% do salário')