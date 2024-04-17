lado1 = int(input('digite o tamanho do primeiro lado do triangulo: '))
lado2 = int(input('digite o tamanho do segundo lado do triangulo: '))
lado3 = int(input('digite o tamanho do terceiro lado do triangulo: '))

if lado1 + lado2 > lado3 or lado1 + lado3 > lado2 or lado2 + lado3 > lado1:
    if lado1 == lado2 and lado2 == lado3:
        print('os lados formam um triagulo equilatero.')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('os lados formam um triangulo isósceles.')
    else:
        print('os lados formam um triangulo escaleno.')
else:
    print('os lados não formam um triangulo.')
        
