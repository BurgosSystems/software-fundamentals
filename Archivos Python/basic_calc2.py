#Algoritm description:
'''
   Basic calc v1
   Get two numbers
   Add, subs, mult, div
   Print results
'''

#1. Initialize vars and/or const (Inputs)
#Escribir " Enter number 1: " //show message from pc to user 
#Leer num1 // User enter a number and program reads it
#print ("please, enter number 1:")
num1 = float(input("Please, enter number 1:"))
#print(type(num1))

#Escribir " Enter number 2: " //show message from pc to user 
#Leer num2 // User enter a number and program reads it
#print ("please, enter number 2:")
num2 = float(input("Please, enter number 2:"))
#print(type(num2))

#2. Processes
add = num1 + num2
subs = num1 - num2 
mult = num1 * num2
div = num1 / num2

#3. Outputs without f-string
print (" Addition: ", add, type(add)) 
print ("Subtraction: ", subs, type(subs))
print ("Multiplication: ", mult, type(mult))
print ("Division: ", div, type(div))

#Output with f string
print ("\n")
print (f" Addition: {add}") 
print (f"Subtraction: {subs}")
print (f"Multiplication: {mult}")
print (f"Division: {div}")