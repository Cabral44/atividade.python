print('tabuada')

c = 0

numero=int(input('qual tabuada você quer saber? digite um numero de 1 a 10. '))

print('tabuada do ',numero,)
while c < 10:
    c = c + 1
    r = numero * c
    print(numero, 'x' ,c, '=', r)
