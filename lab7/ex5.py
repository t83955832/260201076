definepass="aBc123454123123def"
upperCt=0
lowerCt=0
nmbrCt=0
if len(definepass)<8:
    print("Your password is invalid")
else:
    for i in definepass:
        if i.upper()==i:
            upperCt+=1
        elif i.lower()==i:
            lowerCt+=1
        if i.isdigit():
            nmbrCt+=1

print(upperCt,lowerCt,nmbrCt)

if upperCt==0 or lowerCt==0 or nmbrCt==0:
    print("Your password is invalid")
else:
    print("Your Password is valid")







