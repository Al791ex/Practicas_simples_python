""" 
La pizzeria BELLANAPOLIS ofrece pizzas vegetarianas y no vegetarianas a sus clientes, los ingredientes son:
ingredientes vegetarianos: primiento y tofu
ingredientes no vegetarianos: pepperoni, jamon y salmon
pregunte al usuario si quiere ordenar la pizza y de que tipo y que le muestre un menu con los ingredientes
para que elija. Solo se puede elegir un ingrediente ademas de la mozzarella y el tomate que esta en todas las pizzas
al final se debe mostrar si la pizza es vegetariano o no y los ingredientes que lleva.
"""

print("Bienvenido a la pizzeria BELLANAPOLIS!!")
vegetales = {1:"Pimiento", 2:"Tofu"}
carne = {1:"Pepperoni", 2:"Jamon", 3:"Salmon"}
Ving = []
Cing = []

def vegetariana():
    print("Los ingredientes disponibles para las pizzas VEGETARIANAS son: ")
    print(vegetales)
    index = int(input("Selecciona algun ingrediente (1-2): "))
    
    agregar = input("Desea agregar algun otro ingrediente? (s/n): ")
    if agregar == 's':
        Ving.append(vegetales[index])
        print("Los ingredientes disponibles para las pizzas VEGETARIANAS son: ")
        print(vegetales)
        index = int(input("Selecciona algun ingrediente (1-2): "))
        Ving.append(vegetales[index])

    print("\nConfirma tu compra: ")
    print("Pizza VEGETARIANA con los siguientes ingredientes:")
    print(f'- Salsa de tomate\n- Queso mozzarela\n- {Ving}')

    print("Muchas gracias por su pedido!!")

def noVegetariana():
    print("Los ingredientes disponibles para las pizzas NO VEGETARIANAS son: ")
    print(carne)
    index = int(input("Selecciona algun ingrediente (1-3): "))
    agregar = input("Desea agregar algun otro ingrediente? (s/n): ")

    if agregar == 's':
        Cing.append(carne[index])
        print("Los ingredientes disponibles para las pizzas VEGETARIANAS son: ")
        print(carne)
        index = int(input("Selecciona algun ingrediente (1-2): "))
        Cing.append(carne[index])

    print("\nConfirma tu compra: ")
    print("Pizza  NO VEGETARIANA con los siguientes ingredientes:")
    print(f'- Salsa de tomate\n- Queso mozzarela\n- {Cing}') 
    print("Muchas gracias por su pedido!!")

while True:
    print("1. Vegetariana")
    print("2. No Vegetariana")
    pizza = int(input("Seleccione el tipo de pizza que desea ordenar (1 o 2): "))

    if pizza == 1:
        vegetariana()
        break

    elif pizza == 2:
        noVegetariana()
        break

    else:
        print("La opcion que selecciono no existe, intentelo de nuevo...\n")
