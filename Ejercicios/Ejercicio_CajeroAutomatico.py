""" 
Realice un programa que simule un cajero automatico que tenga:
1. Validacion por contraseña
2. ingreso 
3. retiro
4. pregunte que tipo de billete va a retirar
"""
import random as rand

def validacion(user, contra):
    if user == "Alex" and contra == "123": return True
    else: return False

def prestamo():
    if rand.randint(0,2): return True
    else: return False

def ingreso():
    print("0. Dolares ($)")
    print("1. Euros (€)")
    print("2. Libras esterlinas (£)")
    print("3. Bolivares (Bs)")
    y = int(input("Selecciona el tipo de moneda a INGRESAR: "))
            
    ingreso = float(input(f"Ingresa la cantidad de {money[y]} a INGRESAR: "))

    saldo[money[y]] = saldo[money[y]]+ingreso
    print(f"Su saldo actual es: {saldo}")

def confirmacion():
    z = input("\nDesea realizar alguna otra operacion? (s/n): ")
    if z[0] != 's':
        print("Gracias por su visita!!")
        return True
        
def retiro():
    print("0. Dolares ($)")
    print("1. Euros (€)")
    print("2. Libras esterlinas (£)")
    print("3. Bolivares (Bs)")
    y = int(input("Selecciona el tipo de moneda a RETIRAR: "))
            
    retiro = float(input(f"Ingresa la cantidad de {money[y]} a RETIRAR: "))
            
    if saldo[money[y]] >= retiro:
        saldo[money[y]] = saldo[money[y]]-retiro
        print(f"Su saldo actual es: {saldo}")
    else:
        solicitud = input("El monto que ingreso es superior a los fondos disponibles en la cuenta, desea realizar una solicitud de prestamo? (s/n): ")
        if solicitud == 's': 
            solicitud = prestamo()
            if solicitud:
                saldo[money[y]] = saldo[money[y]]-retiro
                print(f"Su saldo actual es: {saldo}")
                        
            else: print("Tu solicitud de prestamo ha sido rechazada...\n")

def saldo():
    print(f"Su saldo actual es: {saldo}")

print("CAJERO AUTOMATICO")
money = ["Dolares ($)","Euros (€)","Libras esterlinas (£)","Bolivares (Bs)" ]
saldo = {money[0]:10, money[1]:15, money[2]:20, money[3]:25}

while True:
    user = input("Ingresa tu usuario: ")
    clave = input("Ingresa tu clave: ")
    val = validacion(user,clave)
    if val == True:
        print("Bienvenido Alex!")
        print("Que desea realizar: ")
        break
    else:
        print("Clave o usuario invalido, intentalo de nuevo: ")

while True:
        print("\n1. Ingresar $$")
        print("2. Retirar $$")
        print("3. Mostrar saldo")
        x = int(input("Selecciona la opcion: "))

        if x == 1:
            ingreso()
            if confirmacion():
                break
                
        if x == 2:
            retiro()
            if confirmacion():
                break

        if x == 3:
            saldo()
            if confirmacion():
                break
            
        else: print("La opcion que ingreso no existe, intente de nuevo...")



    



