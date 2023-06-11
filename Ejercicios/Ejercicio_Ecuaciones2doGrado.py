import math

print("Calculadora de Ecuaciones de 2do Grado...")

# Se ingresan los datos por teclado
a = float(input("\nIntroduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
c = float(input("Introduce el valor de c: "))

# Uso de las funciones + las operaciones pertinentes
parte1 = math.pow(b,2)
parte2 = parte1-4*a*c
if (parte2<0):
    print(f'La ecuacion no tiene solucion real...')
else:
    
    raiz = math.sqrt(parte2)

    # Resultados
    x1 = (-b+raiz)/(2*a)
    x2 = (-b-raiz)/(2*a)

    # Imprimir por pantalla los resultados
    print("\nEl resultado de la operacion es: ")
    print("x1 = " + str(x1))
    print("x2 = " + str(x2))

