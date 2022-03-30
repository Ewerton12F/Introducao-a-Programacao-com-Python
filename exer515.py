# Exercício 5.15 Escreva um programa para controlar uma pequena máquina 
# registradora. Você deve solicitar ao usuário que digite o código do produto e 
# a quantidade comprada. Utilize a tabela de códigos a seguir para obter o preço
# de cada produto:

# | Código | Preço |
# | ------ | ----- |
# | 1      | 0,50  |
# | 2      | 1,00  |
# | 3      | 4,00  |
# | 5      | 7,00  |
# | 9      | 8,00  |

# Seu programa deve exibir o total das compras depois que o usuário digitar 0. 
# Qualquer outro código deve gerar a mensagem de erro "Código inválido".

p = 0
s = 0
s2 = 0
x = 0

while True:
  c = int(input('Informe o código: '))
  
  if c == 0:
    print('Sair')
    break
    
  elif c != 1 and c != 2 and c != 3 and c != 5 and c != 9:
    print('Código inválido!')

  else:
    q = int(input('Informe a quantidade: '))
    if c == 1:
      p = 0.50
    elif c == 2:
      p = 1 
    elif c == 3:
      p = 4
    elif c == 5:
      p = 7
    elif c == 9:
      p = 8
    s = q * p
    s2 += s
  print(f'O total de compras foi de R${s2:.2f}')