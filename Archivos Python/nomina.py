####NOMBRES####
###Edwin Burgos###
###Andres Bucheli###
###Nicolas Garcia###
###Andres chalacan###
#####################
aaaa = 0
currentyear = 2025
age = -1
new = "s"
gen = "yes"
sumaEmple = 0
contEmpleados = 0
contM = 0
contF = 0
contO = 0
sumaSalarios = 0
sumaEdades = 0
while new == "S" or new == "s":
    age = -1
    print("Porfavor digite su nombre completo")
    nom = input()
    print("Ingrese su correo electronico")
    ema = input()
    print("Ingrese su numero telefonico")
    num = int(input())
    genControl = "yes"
    while genControl == "yes":
        print("Ingrese su genero ")
        print("Masculino (M/m)")
        print("Femenino (F/f)")
        print("Otro (O/o)")
        gen = input()
        if gen == "M" or gen == "F" or gen == "O" or gen == "m" or gen == "f" or gen == "o":
            genControl = "not"
        else:
            print("Respuesta invalida")
            genControl = "yes"
    if gen == "M" or gen == "m":
        contM = contM + 1
    else:
        if gen == "F" or gen == "f":
            contF = contF + 1
        else:
            contO = contO + 1
    print("Ingrese su salario")
    sal = int(input())
    while age < 0 or age > 150:
        print("Porfavor dijite su año de nacimiento: ")
        aaaa = int(input())
        age = currentyear - aaaa
        if age > 0 and age < 150:
            pass
        else:
            print("Edad invalida")
    contEmpleados = contEmpleados + 1
    sumaSalarios = sumaSalarios + sal
    sumaEdades = sumaEdades + age
    print("su edad es de: " + str(age))
    print("Usuario registrado con exito")
    print("Desea agregar otro usuario")
    print("Seleccione: ")
    print("SI (S/s)")
    print("NO (N/n)")
    new = input()
    if new == "S" or new == "s" or new == "N" or new == "n":
        if new == "S" or new == "s":
            new = "s"
        else:
            new = "not"
    else:
        new = "yes"
        while new == "yes":
            print("Respuesta invalida")
            print("Porfavor digite nuevamente su respuesta (S/N)")
            print("Desea agregar otro usuario")
            print("SI (S/s)")
            print("NO (N/n)")
            new2 = input()
            if new2 == "s" or new2 == "S" or new2 == "N" or new2 == "n":
                if new2 == "S" or new2 == "s":
                    new = "s"
                    new2 = "not"
                else:
                    new = "not"
                    new2 = "not"
            else:
                new2 = "yes"
if contEmpleados > 0:
    promEdades = float(sumaEdades) / contEmpleados
else:
    promEdades = 0
print("#####REPORTE#####")
print("Empleados Registrados: " + str(contEmpleados))
print("Total Genero Masculino: " + str(contM))
print("Total Genero Femenino: " + str(contF))
print("Total Genero Otro: " + str(contO))
print("Total Salarios a Pagar: " + str(sumaSalarios))
print("Promedio de Edades: " + str(promEdades))
