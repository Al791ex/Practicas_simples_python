""" Los alumnos de un curso se han dividido en dos grupos A Y B de acuerdo al sexo y el nombre.
El grupo A esta formado por mujeres con un nombre anterior a la 'm' y los hombres con un nombre
posteriora la 'N' y el grupo B por el resto. """

print("Bienvenido alumno, ingresa los siguientes datos...")
nombre =str(input("Ingresa tu nombre: "))
sexo =str(input("Ingresa tu sexo (M/F): "))
i = 0
A = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
A2 = ["N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


if sexo[0] == "F":
    for i in range(26):
        if nombre[0] == A[i]:
            print("Eres del grupo A")
            
if sexo[0] == "M":
    for i in range(28):
        if nombre[0] == A2[i]:
            print("Eres del grupo A")
else:
    print("Eres del grupo B")

    