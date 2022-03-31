# Exercício 5.21 Reescreva o Programa 5.1 de forma a continuar executando até 
# que o valor digitado seja 0. Utilize repetições aninhadas.

valor = int(input("Digite o valor a pagar:"))
cédulas= 0
atual = 50
apagar = valor

while valor != 0:
    while True:
        if atual <= apagar:
            apagar -= atual
            cédulas += 1
        else:
            print(f"{cédulas} cédula(s) de R${atual}")
            if apagar == 0:
                break
            if atual == 50 :
                atual = 20
            elif atual == 20:
                atual = 10
            elif atual == 10:
                atual = 5
            elif atual == 5:
                atual = 1
            cédulas = 0
    valor = int(input("Digite o valor a pagar:"))
    cédulas= 0
    atual = 50
    apagar = valor