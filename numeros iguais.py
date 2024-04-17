print('Faça um programa que receba dois números e mostre qual deles é o maior. Se os dois números forem iguais, imprima a mensagem Números iguais')

numero1 = int(input('digite o primeiro numero:'))
numero2 = int(input('digite o sengundo numero:'))

if(numero1 > numero2 ):
    print('o numero maior é:'+ str(numero1))
elif(numero2 > numero1 ):
    print('o numero maior é:'+ str(numero2))
else:
    print('numeros iguais')
