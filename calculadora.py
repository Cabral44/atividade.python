# Exercício 4 (Calculadora) - Codifique um programa que faça a leitura de dois números
# reais. A seguir o programa lê um caractere, que deve ser +, -,
# * ou /, e realiza a operação
# indicada pelo caractere sobre os valores lidos.

n1 = float(input('digite o primeiro numero: '))
n2 = float(input('digite o segundo numero: '))
sinal = input('digite o sinal da operação que deseja (+,-,* ou /): ')

if sinal == "+":
    resu = n1 + n2
    
elif sinal == "-":
    resu = n1 - n2

elif sinal == "*":
    resu = n1 * n2

elif sinal == "/":
    resu = n1 / n2

else:
    print('operação invalida')

print('O resultado é ',resu)
    
