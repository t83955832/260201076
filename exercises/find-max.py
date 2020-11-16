inputValues=input("Enter three values  seperated with commas ex:(36,52,78)")

x1,x2,x3=inputValues.split(",")

print(x1,x2,x3)
x1=int(x1)
x2=int(x2)
x3=int(x3)


if x1>x2:
    if x1>x3:
        print("most biggest",x1)
    else:
        print("most biggest",x3)
else:
    if x2>x3:
        print("most biggest",x2)
    else:
        print("most biggest",x3)



