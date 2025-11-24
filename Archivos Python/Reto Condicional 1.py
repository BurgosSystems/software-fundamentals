import random
random.seed()   #Prepare random number generator

print("Lanzando los dados")
dado1 = int(random.random() * 6) + 1
dado2 = int(random.random() * 6) + 1
print("Dado1:" + str(dado1))
if dado1 % 2 == 0:
    paroimpar1 = "Par"
    print("El dado 1 es: " + paroimpar1)
else:
    paroimpar1 = "Impar"
    print("El dado 1 es: " + paroimpar1)
print("Dado2:" + str(dado2))
if dado2 % 2 == 0:
    paroimpar2 = "Par"
    print("El dado 2 es: " + paroimpar2)
else:
    paroimpar2 = "Impar"
    print("El dado 2 es: " + paroimpar2)
if dado1 == dado2:
    print("YOU WIN")
else:
    print("GAME OVER")
