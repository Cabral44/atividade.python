print('lição 1')

nota1 = float(input('digite a nota  1: '))
nota2 = float(input('digite a nota  2: '))

if(nota1>= 0 and nota1<= 10 and nota2 >= 0 and nota2 <= 10):
    soma = nota1 + nota2
    media = soma/2

else:
    print('nota invalida')

if(media >= 6):
    print('aprovado')

elif(media < 6 and media >= 4):
    print('Você está de recuperação')

else:
    print('reprovado')


