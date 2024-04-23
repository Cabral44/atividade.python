# Exercício 3-Faça um programa que receba a idade de 5 pessoas e imprima quantas pessoas
# são maiores que 18 anos.
c = 1
n = 0
while c <= 5:
    c = c + 1
    idade = int(input('digite sua idade: '))
    if idade > 18:
        n = n + 1
print('o numero de pessoas maiores que 18 anos são: ',n)



     
