
busPrice=3
getAge=int(input("enter your age"))

if getAge<6 or getAge>=60:
    print("free")
elif 6<=getAge<=18:
    print("50% discount you will pay ",busPrice/2)
else:
    print("you will pay",busPrice)