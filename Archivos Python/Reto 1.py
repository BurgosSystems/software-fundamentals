import random
random.seed()   #Prepare random number generator

dado = int(random.random() * 6) + 1
print("Lanzando el dado")
print("El numero obtenido es: " + str(dado))
if dado % 2 == 0:
    paroimpar = "par"
    print("El dado es par")
else:
    paroimpar = "Impar"
    print("El dado es impar")
