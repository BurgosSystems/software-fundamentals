birthyear = 0
currentyear = 2025
age = -1
age2 = -1
while age < 0 or age > 150:
    print("Porfavor dijite su año de nacimiento: ")
    birthyear = int(input())
    age = currentyear - birthyear
    if age > 0 and age < 150:
        pass
    else:
        print("Edad invalida")
print("su edad es de: " + str(age))
print("confirmar")
res = input()
if res == "si" or res == "ok" or res == "confirmo" or res == "afirmativo" or res == "yes" or res == "listo" or res == "confirmado" or res == "okey" or res == "y" or res == "s" or res == "dale" or res == "claro" or res == "va":
    pass
else:
    while res == "no":
        print("Porfavor dijite su año de nacimiento: ")
        birthyear2 = int(input())
        age2 = currentyear - birthyear2
        if age2 > 0 and age2 < 150:
            print("su edad es de: " + str(age2))
            print("confirmar")
            res = input()
            if res == "si" or res == "ok" or res == "confirmo" or res == "afirmativo" or res == "yes" or res == "listo" or res == "confirmado" or res == "okey" or res == "y" or res == "s" or res == "dale" or res == "claro" or res == "va":
                pass
            else:
                print("Demasiados intentos")
        else:
            print("Edad invalida")
            res = "no"
