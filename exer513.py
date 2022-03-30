# Exercício 5.13 Escreva um programa que pergunte o valor inicial de uma dívida e
# o juro mensal. Pergunte também o valor mensal que será pago. Imprima o número 
# de meses para que a dívida seja paga, o total pago e o total de juros pago.

import math

divida = float(input('Valor da dívida inicial: R$ '))
juros = float(input('Valor do juros: % '))
pag = float(input('Valor pago ao mês: R$ '))

dividajuros = divida + (divida * (juros/100))
meses = math.ceil(dividajuros / pag)

print(f'''
    A divida será paga em {meses} meses.
    O total pago será de R$ {dividajuros:.2f}.
    O total de juros pago é de R$ {dividajuros - divida:.2f}.
''')