enterYear=int(input(""))

a=enterYear%100
if a%4!=0 and enterYear%400!=0:
    print("not leap years")
else:
    print("leap years")