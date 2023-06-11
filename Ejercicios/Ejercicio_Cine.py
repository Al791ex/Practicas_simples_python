""" Elabore un programa que simula la ventas de boletos de un empresa de entretenimiento (CINE), donde el valor de los boleto dependera de la clasificacion de la pelicula

A = 2$ 

B = 3$ 13

C = 3.5$ a partir de 

D y E = 5$

se aplicara descuento los dias lunes, jueves y viernes del 20%

Se aplicara descuento por niño y 3era edad de 50% """

print("Bienvenido a Cines Unidos!!")

# 1 -> A \ 2 -> B \ 3 -> C \ 4 -> D y E   
clasificacion = {1:2, 2:3, 3:3.5, 4:5}
boleto = {1:1, 2:0.50, 3: 0.50}
dia = {1:0.80, 2:1, 3:1, 4:0.80, 5:0.80, 6:1, 7:1}
boletos = ["Boleto general", "Boleto infantil", "Boleto 3era edad"]
snack = ["Cubo de palomita", "Refresco", "Paquete de caramelos", "Barra de chocolate"]
carrito = []
boleto_text = {}
while True:
    print("\n~~Menu~~")
    print("1. Comprar boletos\n2. Snacks\n3. Revisar carrito\n4. Salir")
    opcion = int(input("Selecciona una opcion (1-4): "))
    
    
    if opcion == 1:
        while True:
            print("\n~~CARTELERA~~")
            print("1. Pinocchio [A]\n2. Avengers: Endgame [B]\n3. It [C]\n4. La huesera [D]\n5. 50 sombras mas oscuras [E]")
            pelicula = int(input("Selecciona alguna de las peliculas disponibles (1-5):"))
            
            print("\n1. Lunes\n2. Martes\n3. Miercoles\n4. Jueves\n5. Viernes\n6. Sabado\n7. Domingo")
            dia_index = int(input("Selecciona el dia de la función (1-7): "))
            
            print("\nCompra tus boletos :)")
            print("1. Boleto general")
            print("2. Boleto infantil (3-12 años)")
            print("3. Boleto 3era edad (a partir de 60 años)")
            boleto_index = int(input("Selecciona una opcion (1-3): "))
            boletos_cantidad = int(input("Ingresa la cantidad de boletos: "))
            
            
            precio = clasificacion[pelicula]*boleto[boleto_index]
            precio_boletos = precio*boletos_cantidad
            precio_total = precio_boletos*dia[dia_index]
            
            boleto_text = {boletos[boleto_index]:boletos_cantidad}
            carrito.append(boleto_text)

            print(f'Su compra:\n{boleto_text}\nEl precio total es: {precio_total}')
            x = input("Desea comprar algun otro boleto? (s/n): ")
            if x[0] != 's':
                break

    elif opcion == 2:
        print("\n~~SNACKS~~")
        print("1. Cubo de palomitas \n2. Refresco\n3. Paquete de caramelos\n4. Barra de chocolate")
        snack_index = int(input("Selecciona una opcion (1-4): "))
        snack_cantidad = int(input("Ingresa la cantidad: "))
        snack_text = {snack[snack_index]:snack_cantidad}
        carrito.append(snack_text)
    elif opcion == 3:
        print("\n~~CARRITO~~")

        if boleto_text:
            print("Boletos:")
            print(boleto_text)

        elif snack_text:
            print("Snacks: ")
            print(snack_text)
            
        else:
            print("Actualmente no posees ninguna compra...")
        
    elif opcion == 4:
        break

    else:
        (print("La opcion seleccionada no existe, intentalo de nuevo..."))
            




