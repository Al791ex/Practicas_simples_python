""" 
Escribir un programa que reciba una cadena de caracteres, y devuelva un diccionario con cada palabra que contiene
y su frecuencia. Escribir otra funcion que reciba el diccionario generado con la funcion anterior y devuelva una tupla con la palabra
mas repetida y su frecuencia.
"""

def diccionario_palabras(cadena):
    lista = cadena.split()
    n = len(lista)
    dicc = {}
    
    for i in range (0,n):
        cantidad = lista.count(lista[i])
        print(cantidad)
        #dicc[lista[i]] = cantidad
        
    print(dicc)

cadena = input("Ingresa un cadena de caracteres: ")

diccionario_palabras(cadena)









        











