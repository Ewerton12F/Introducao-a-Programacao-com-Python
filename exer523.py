# Exercício 5.23 Escreva um programa que leia um número e verifique se é ou não 
# um número primo. Para fazer essa verificação, calcule o resto da divisão do 
# número por 2 e depois por todos os números ímpares até o número lido. 
# Se o resto de uma dessas divisões for igual a zero, o número não é primo. 
# Observe que 0 e 1 não são primos e que 2 é o único número primo que é par.

n = int(input(''))
div = 0
x = 1
divisores = list()

while x <= n:
    if x <= 2:
        x += 1
    else:
        x += 2
    
    if n % x == 0:
        div += 1
        divisores.append(x)

if div == 1 or div == 0:
    print(f'{n} é primo!')
else:
    print(f'{n} não é primo! Os divisores são {divisores}')