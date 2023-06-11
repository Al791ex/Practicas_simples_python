""" 
Escriba una funcion que calcule el area de un circulo y otra que calcule el volumen de un cilindro usando
la primera funcion
"""
import math

def area_circulo(radiocir):
    area = math.pi*(math.pow(radiocir,2))
    print(f'El area del circulo es: {area}')

def volumen_cilindro(radiocil,h):
    volumen = math.pi*(math.pow(radiocil,2))*h
    print(f'El area del volumen del cilindro es: {volumen}')



while True:

    radiocir = int(input("Ingresa el radio del circulo: "))
    area_circulo(radiocir)

    radiocil = int(input("Ingresa el radio del cilindro: "))
    h = int(input("Ingresa el la altura del cilindro: "))
    volumen_cilindro(radiocil,h)

    
    x = input("Desea seguir calculando? (s/n): ")
    if x[0] != 's':
        break

