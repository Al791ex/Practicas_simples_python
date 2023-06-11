""" 
Escriba un programa que  realice la funcion del total de la factura, la funcion debe recibir la cantidad
sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura, si se invoca la funcion sin
pasar el porcentaje de IVA el cliente debera pagar 21%
"""

def iva_variable(can_fact):
    cant_iva = float(input("Ingresa el porcentaje de IVA a aplicar: "))
    monto = can_fact*cant_iva/100
    montof = can_fact-monto
    print("\nFACTURA")
    print(f"El monto total con IVA del {cant_iva}% es: {montof}")

def iva_default(can_fact,cant_iva=21):
    monto = can_fact*cant_iva/100
    montof = can_fact-monto
    print("\nFACTURA")
    print(f"El monto total con IVA del {cant_iva}% es: {montof}")


while True:
    can_fact = float(input("\nIngresa la cantidad en bs: "))
    aux = (input("Desea agregar un porcentaje de IVA especifico? (s/n): "))

    if aux[0] == 's':
        iva_variable(can_fact)
    else:
        iva_default(can_fact)

    aux2 = input("Desea realizar otra factura? (s/n): ")
    if aux2 != 's':
        break






