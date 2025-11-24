import random
random.seed()   #Prepare random number generator

print("Ingrese el número de lanzamientos: ")
n = int(input())
suma = 0
for i in range(1, n + 1, 1):
    dado = int(random.random() * 6) + 1
    suma = suma + dado
    print("El dado " + str(i) + " salio: " + str(dado))
