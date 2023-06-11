""" 
En un colegio se requiere postulante para un equipo de basquetbol que los represente, son requisitos indispensables:
- Menor o igual a 19 anios
- Estatura mayor o igual a 175cm
- Su peso entre 75 y 80 kilos
Se requiere un programa que diga cuantos postulantes son aprobados, cuantos son reprobados y cuantos cumplen por lo menos 
2 condiciones.
"""
#Enunciado
print("EQUIPO DE BASQUETBOL")
print("POSTULANTES\n")

#contador para n postulantes y arrays
n = 1
aprobados = []
reprobados = []
cumplen = []

#Bucle infinito para que el programa no pare hasta que se indique
while True:
    
    #Se piden datos al usuario
    print(f"Postulante n{n}")
    nombre = input("Ingrese su nombre: ") 
    edad = int(input("Ingrese su edad: "))
    estatura = float(input("Ingrese su estatura en CM: "))
    peso = float(input("Ingrese su peso en KG: "))
    
    #Se comparan los datos con las especificaciones dadas
    if edad <= 19 and estatura >= 175 and peso >= 75 and peso <=80:
        #Se agrega a un array [aprobados]
        aprobados.append(nombre)
        
    #Se verifica si cumple alguna de las 2 condiciones
    elif edad <= 19 and estatura >= 175:
        cumplen.append(nombre)
      
    elif edad <= 19 and peso >= 75 and peso <=80:
        cumplen.append(nombre)
    
    elif estatura >= 175 and peso >= 75 and peso <=80:
        cumplen.append(nombre)
        
    else:
        #Se agrega a un array [reprobados]
        reprobados.append(nombre)
    
    #Se pregunta al usuario si quiere agregar postulantes
    x = input("Desea agregar otro postulante? (s/n): \n")
    
    if x[0] == 's':
        n+=1
    else:
        break

#Se cuentan el numero de elementos dentro de los arreglos
na = len(aprobados)
nr = len(reprobados)
nc = len(cumplen)

#Se imprimen los datos dentro de las variables usadas para almacenar la cantidad de postulados y los nombres de los mismos
print(f'\nLas postulantes APROBADOS son {na} :{aprobados}')
print(f'Las postulantes REPROBADOS son {nr} :{reprobados}')  
print(f'Las postulantes que CUMPLEN con 2 CONDICIONES son {nc} :{cumplen}')  
        

        
    
    