# variable declaration
# data entry into variables
print("Enter document type")
tiDo = input()
print("Enter ID number")
nume = input()
print("Enter names")
noms = input()
print("Enter last names")
apels = input()
print("Enter gender")
gen = input()
print("Year of birth")
aNa = int(input())
print("Address")
direc = input()
print("Phone")
tel = input()
print("Salary")
sala = float(input())

# variable salary comparison for performing operations
if sala >= 2000000:
    if gen == "female":
        inc = sala * 3 / 100
        nueSala = sala + inc
        print("The salary of  " + noms + "  " + apels + "  is " + str(nueSala))
    else:
        inc = sala * 2.5 / 100
        nueSala = sala + inc
        print("The salary of  " + noms + "  " + apels + "  is " + str(nueSala))
else:
    if sala > 1200000 or sala > 2000000:
        inc = sala * 5 / 100
        nueSala = sala + inc
        print("The salary of  " + noms + "  " + apels + "  is " + str(nueSala))
    else:
        if gen == "female":
            inc = sala * 10 / 100
            nueSala = sala + inc
            print("The salary of  " + noms + "  " + apels + "  is " + str(nueSala))
        else:
            inc = sala * 8 / 100
            nueSala = sala + inc
            print("The salary of  " + noms + "  " + apels + "  is " + str(nueSala))
