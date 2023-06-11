#Realice un programa que vaya de uno hasta n que clasifique varios tipos de animales.

n = int(input("Ingresa la cantidad de animales:"))

h = []
c = []
o = []

for i in range (n):
    animal = input("Ingresa el animal: ")

    herviboro = input("Es Herviboro? (s/n): ")
    if herviboro == 's':
        h.append(animal)
    elif herviboro == 'n':
        carnivoro = input("Es Carnivoro? (s/n): ")
        if carnivoro == 's':
            c.append(animal)
            omnivoro = input("Es Omnivoro? (s/n): ")
    elif omnivoro == 's':
        o.append(animal)
            

    

print("\nAnimales\n")
print(f'Herviboros: {h}')
print(f'Carnivoros: {c}')
print(f'Omnivoros: {o}')
        


    

    


