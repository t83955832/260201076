definePassword="abc123"
while True:
    password=input("Please enter your password : ")
    if password==definePassword:
        print("Welcome")
        break
    else:
        if password=="help":
            print(str(definePassword[0]))
        else:
            print("Wrong")
            

