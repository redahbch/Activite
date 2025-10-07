def F1(n):
    for i in range(n):
        print("Bonjour ")

def F2(n):
    if n%10==0:
        print("l'entier est divisible par 10")
    else :
        print("l'entier n'est pas divisible par 10")

def F3(chaine):
    min=['a','e','u','i','o']
    comp=0
    for char in chaine:
        if char in min :
            comp+=1
    print(comp)

def F4(n):
    fact=1
    for i in range (1,n+1):
        fact=fact*i

    return fact

def F5(n):
    for i in range(10):
        print(f"{n} * {i} = {n*i}")

def F6(chaine):
    comp=0
    for i in range(len(chaine)):
        comp+=1
    print(f"ce mot est compose de {comp} caracteres")

def F7(n):
    U0=1
    U1=2
    if n==0:
        print(1)
    for i in range(2,n+1):
        tem=U1
        U1=U1+U0
        U0=tem
    print(U1)

    
