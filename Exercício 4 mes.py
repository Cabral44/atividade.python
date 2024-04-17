# Criar um programa que leia um número inteiro entre 1 e 12 e escrever o mês
# correspondente. Caso o usuário digite um número fora desse intervalo, deverá aparecer
# uma mensagem informando que não existe mês com este número.
mes = int(input('digite um numero entre 1 a 12.'))

if(mes == 1):
    print('janeiro')
elif(mes == 2):
    print('fevereiro')
elif(mes == 3):
    print('março')
elif(mes == 4):
    print('abril')
elif(mes == 5):
    print('maio')
elif(mes == 6):
    print('junho')
elif(mes == 7):
    print('julho')
elif(mes == 8):
    print('agosto')
elif (mes == 9):
    print('setembro')
elif(mes == 10):
    print('outubro')
elif(mes == 11):
    print('novenbro')
elif(mes == 12):
    print('dezenbro')
else:
    print('numero do mes invalido.')
