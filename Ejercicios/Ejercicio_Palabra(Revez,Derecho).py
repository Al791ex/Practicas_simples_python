""" 
Escriba un programa que pida al usuario una palabra y muestre una a una las letras,
empezando por la ultima.
"""

def revez(palabra):
    print("Palabra al revez: ")
    n = len(palabra)
    aux = n-1
    while n > 0:
        print(palabra[aux])
        aux-=1
        n-=1

def derecho(palabra):
    print("Palabra al derecho: ")
    for i in palabra:
        print(i)


palabra = input("Ingresa una palabra: ")
revez(palabra)
derecho(palabra)













