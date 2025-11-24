def numbers():
    add=0
    i=1
    while i<=100:
        add+=i
        i+=1
    return add

###main###
total=numbers()
print(f"Total:{total}")