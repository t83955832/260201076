defined_pass="abc123"
ct=0
while ct!=3:
    ct+=1
    userpass=input("Enter your password").lower()
    if userpass==defined_pass:
        print("You have successfully logged in")
        break
    else:
        print("Sorry, the password is wrong")
        if ct==3:
            print("You have been denied access")
            break
        

        


