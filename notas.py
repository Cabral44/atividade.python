nota = int(input('digite a nota:'))

if(nota >= 86 and nota <= 100):
    print('nota: A')
elif(nota >= 61 and nota <= 85):
    print('nota: B')
elif(nota >= 36 and nota <= 60):
    print('nota: C')
elif(nota >= 1 and nota <= 35):
    print('nota: D')
else:
    print('nota: E')
