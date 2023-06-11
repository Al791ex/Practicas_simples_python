import math
print("Programa para hallar la hipotenusa de un triangulo")
a= float(input("\nIngresa el valor del cateto adyacente: "))
b= float(input("Ingresa el valor del cateto opuesto: "))

x = math.pow(a,2)+math.pow(b,2)
h = math.sqrt(x)

print("La hipotenusa es: " + str(h))