print("please enter number: ")
num = float(input())
if num > 0:
    if num % 2 == 0:
        print("The first number positive  " + str(num) + " it's even")
    else:
        print("The first number positive  " + str(num) + " It's odd")
else:
    if -num % 2 == 0:
        print("The first number negative  " + str(num) + " it's even")
    else:
        print("The first number negative  " + str(num) + " It's odd")
