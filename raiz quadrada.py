import math
n = int(input('Digite um número:'))
if n < 0:
   print('Número inválido.')
else:
   raiz = math.sqrt(n)
   print(f'A raiz quadrada de {n} é {raiz}') 
