import math
'''
Menu con 4 opciones, sin usar librerias
1.Area de un circulo
2.Imprimir el abecedario
3.Imprimir numeros primos  1 a 300
4.Ejercicio de caida libre, piscina y hombre tirandose a altura x, calcular velocidad del hombre cayendo
'''
while True:

    print("MENU")
    print("1. Area de un circulo")
    print("2. Imprimir el Abecedario")
    print("3. Numeros primos del 1 al 300")
    print("4. Caida libre")
    x =int(input("Ingresa la opcion a elegir: "))

    if x == 1:
        radio = float(input("Ingresa el radio: "))
        area = math.pi*(radio**2)
        print(f'El radio de tu circunferencia es de: {area}')
        
    elif x == 2:
        abecedario = []
        for i in range(65,91):
            Ascii = chr(i)
            abecedario.append(Ascii)  
        print(abecedario)
            
    elif x == 3:
        primos = []
        for i in range (1,301):
            contador = 0
            for j in range (2,i):
                mod = i%j
                if mod == 0:
                    contador += 1
            if contador == 0:
                primos.append(i)    
        print(primos)

    elif x == 4:
        h= float(input("Ingresa la altura del ejercicio: "))
        aux = input("Deseas ingresar la gravedad o usar la predeterminada? '9,8m/s2' (s/n): ")
        if aux[0] != 's':
            g = float(input("Ingresa la gravedad: "))
        else:
            g = 9.8
        v = math.sqrt(2*g*h)
        print(f'La velocidad es: {v} m/s2')

    else: print("\nLa opcion seleccionada no existe, intentalo de nuevo..\n")

    z = input("Desea realizar otra operacion? (s/n): ")

    if z[0] != 's':
        break