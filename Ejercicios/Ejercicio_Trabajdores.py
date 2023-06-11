print("Bienvenido trabajador...")
nombre = (input("Ingresa tu nombre: "))
sueldo = 2400
while True:
    puntaje = (float(input("Ingresa tu puntaje (0.0)/(0.4)/(0.6 o mas): ")))
    if puntaje == 0.0 or puntaje == 0.4 or puntaje == 0.6 or puntaje>0.6: 
        break
    else:
        print("Entrada invalida, intentalo de nuevo...")

if puntaje == 0.0:
    print(str(nombre)+" tu puntaje es inaceptable, tu sueldo es: "+ (str(sueldo*puntaje)+"$"))

if puntaje == 0.4:
    print(str(nombre)+" tu puntaje es Aceptable, tu sueldo es: "+ (str(sueldo*puntaje)+"$"))

if puntaje == 0.6:
    print(str(nombre)+" tu puntaje es Meritorio, tu sueldo es: "+ (str(sueldo*puntaje)+"$"))