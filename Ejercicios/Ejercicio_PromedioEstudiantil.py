# Ingresa por consola 4 notas y calcular el promedio
print("Promedio de las notas de 4 estudiantes")
n1 = float(input("\nIngresa la nota del primer estudiante: "))
n2 = float(input("Ingresa la nota del segundo estudiante: "))
n3 = float(input("Ingresa la nota del tercer estudiante: "))
n4 = float(input("Ingresa la nota del cuarto estudiante: "))

nota = (n1+n2+n3+n4)/4

print("El promedio de todas las notas es: " + str(nota))