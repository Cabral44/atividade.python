#2- Escreva um programa que leia três números e mostre o maior e o menor deles.

n1 = int(input('digite o primeiro numero: '))
n2 = int(input('digite o segundo numero: '))
n3 = int(input('digite o terceiro numero: '))


if (n1 > n2 and n1 > n3):
    maior = n1
if (n2 > n1 and n2 > n3):
   maior =n2
if (n3 > n1 and n3 > n3):
   maior =n3
if (n1 < n2 and n1 < n3):
    menor = n1
if (n2 < n1 and n2 < n3):
   menor =n2
if(n3 < n1 and n3 < n3):
   menor =n3

print('o numero maior é',maior)
print('o numero menor é',menor)
