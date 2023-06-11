""" 
realizar un programa que reciba x cantidad de datos y luego los ordene 
"""

conjunto_datos = []
print("Hola!")

while True:

    datos = input("Ingresa un dato: ")
    conjunto_datos.append(datos)
    print(conjunto_datos)
    aux = input("Deseas ingresar otro dato? (s/n): ")
    if aux[0] != 's':
        print("Hasta luego!!")
        break  

conjunto_datos.sort()

print(f'El conjunto de datos ordenados es: {conjunto_datos}')



