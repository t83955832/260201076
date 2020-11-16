a=int(input("ENTER 1 : "))
b=int(input("ENTER 2 : "))
degit=0

while a>0 and b>0:
    if a%10==b%10:
        degit+=1

    a//=10
    b//=10


print(degit)
    



