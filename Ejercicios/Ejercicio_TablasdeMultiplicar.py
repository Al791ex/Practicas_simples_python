#Usar bucles para hacer las tablas de multiplicar

print("Tablas de multiplicar")

for i in range (1, 10):

    for x in range (1,10):
        resultado = i*x

        print (f'{i} x {x} = {resultado}')
        if x == 9:
            print('\n')
        


