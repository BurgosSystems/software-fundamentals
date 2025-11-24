print("please enter number positive or negative")
num = float(input())
if fabs(num) % 2 == 0:
    paroimpar = "even"
    print("the number is: " + paroimpar)
else:
    paroimpar = "odd"
    print("the number is: " + paroimpar)
