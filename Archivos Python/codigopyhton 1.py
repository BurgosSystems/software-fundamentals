import random

print("lanzando dados")

Numero1 = random.randint(1, 6)
Numero2 = random.randint(1, 6)

print("DADO1: " + str(Numero1))

if Numero1 % 2 == 0:
    print("par")
else:
    print("impar")

print("DADO2: " + str(Numero2))

if Numero2 % 2 == 0:
    print("par")
else:
    print("impar")

# Determinar el resultado del juego
if Numero1 == Numero2:
    print("Ganaste")
else:
    print("Perdiste")