# 1- Escreva um programa que leia três números e mostre o maior deles.

n1 = int(input('digite o primeiro numero: '))
n2 = int(input('digite o segundo numero: '))
n3 = int(input('digite o terceiro numero: '))

if (n1 > n2 and n1 > n3):
    print('o maior numero é',n1)
elif (n2 > n1 and n2 > n3):
    print('o maior numero é',n2)
else:
    print('o maior numero é',n3)
