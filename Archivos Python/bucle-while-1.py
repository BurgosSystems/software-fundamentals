import os
os.system("clear")
status=True
acum=0
numT=0
par=0
impar=0
parPos=0
parNeg=0
ImParPos=0
imParPos=0
imParNeg=0
nega=0
posi=0
posiImpa=0
negaImpa=0
while status: 
    print ("press my number (0 to exit):")
    num=int (input())
    acum+=num
    numT=numT+1
    if num%2==0:
        par=par+1
        if num>0:
            parPos=parPos+1
            posi=posi+1
        else: 
            parNeg=parNeg+1
            nega=nega+1    
    else: 
        if num>0:
            imParPos=imParPos+1
            posiImpa=posiImpa+1
        else:
            imParNeg=imParNeg+1
            negaImpa=negaImpa+1
        impar=impar+1
    if num==0:
        status=False
print("total:", acum)
print("total de numeros digitados:", numT-1)
print("total de pares digitados:", par-1)
print("total de impares digitados:", impar)
print("total de positivos digitados:", posi+posiImpa)
print("total de negaticos digitados:", (nega+negaImpa)-1)
print("total de pares positivos digitados:", parPos)
print("total de pares negativos digitados:", parNeg-1)
print("total de impares negativos digitados:", imParPos-1)
print("total de impares positivos digitados:", imParNeg)