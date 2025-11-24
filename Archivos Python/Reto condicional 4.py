# Declare variables or constants
# Variable to assign opt value (Between i and 5)
# Initilize variables or constants
num1 = 0
num2 = 0

# Get number 1
print("Enter value to number 1:")
num1 = float(input())

# Get number 2
print("Enter value to number 2:")
num2 = float(input())

# Print math menu
print("Math menu: [1]. Add - [2]. Subs - [3]. Mult - [4]. Div - [5] All")
print("Press any option [1-5]")
opt = int(input())
if opt == 1:
    res = num1 + num2
    print("Addition:" + str(res))
else:
    if opt == 2:
        res = num1 - num2
        print("Substraction:" + str(res))
    else:
        if opt == 3:
            res = num1 * num2
            print("Multiplication:" + str(res))
        else:
            if opt == 4:
                if num2 == 0:
                    print("It is not possible to divide by zero")
                else:
                    res = num1 / num2
                    print("Division: " + str(res))
            else:
                if opt == 5:
                    if num2 == 0:
                        print("Add: " + str(num1 + num2))
                        print("Subs: " + str(num1 - num2))
                        print("Mult: " + str(num1 * num2))
                        print("Div: El numero 2 no puede ser " + str(num2))
                    else:
                        print("Add: " + str(num1 + num2))
                        print("Subs: " + str(num1 - num2))
                        print("Mult: " + str(num1 * num2))
                        print("Div: " + str(num1 / num2))
                else:
                    print("Option invalid")
