def myFile():
    file                        =   open("users.txt","r")
    users                       =   {}
    username,password,friends   =   [],[],[]

    for _ in file:
        username            =   _.split(";")[0]
        password            =   _.split(";")[1]
        friends             =   _.split(";")[2].replace("\n","")
        users[username]     =   password+"-"+friends
    
    return users





def check_user():
    users=myFile()
    name=input("Please enter username:\n")
    pas=input("Please enter password:\n")
    isLog(users,name,pas)
    if name in users.keys():
        if pas == str(users[name].split("-")[0]):
            print("Logged in\n")
            main()
        else:
            print("Wrong password or username\n")
    else:
        print("Wrong password or username\n")

    


def isLog(users,name,pas):
    list_of_users=[]
    print(users)



def createNewUser():
    users=myFile()
    file=open("users.txt","a")
    name=input("Please enter username:\n")
    pas=input("Please enter password:\n")

    if name in users.keys():print("Username not valid\n")

    else:
        if name.strip():
            if 4<=len(pas)<=8:
                if pas.isalnum():
                    name.lower()
                    name=name.replace("ç","c").replace("ğ","g").replace("ı","i").replace("ö","o").replace("ş","s").replace("ü","u")
                    file.write(name+";"+pas+";\n")
                else:
                    print("Password not valid\n")
            else:
                pass
        else:
            pass





def main():
    menu_text=int(input("1.Log in / change user\n2.Create new user\n3.Add friend\n4.Show my friends\n5.Exit\n"))
    if menu_text==1:check_user()
    elif menu_text==2:createNewUser()

    elif menu_text==3:
        isLog()
    elif menu_text==4:pass
        

    elif menu_text==5:pass
    else:
        print("Invalid option\n")
        main()

main()