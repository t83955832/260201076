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
friends=myFile()
logged_user=""
def exitt(friends):
  file=open('users.txt','w')
  file_str=''
  for i in friends.keys():
    file_str+=i+';'+friends[i].replace('-',';')+'\n'
  file.write(file_str)
  quit()

def check_username(friends):
    name        =   input("Please enter username:\n")
    isDigit     =   False
    isAlpha     =   False
    if name in friends.keys():
        print("Username not valid\n")
    else:
        name    =   name.strip()
        name    =   name.lower()
        name    =   name.replace("ç","c").replace("ğ","g").replace("ı","i").replace("ö","o").replace("ş","s").replace("ü","u")

        for _ in name:
            if _.isdigit():
                isDigit=True
            if _.isalpha():
                isAlpha=True
        if isDigit or isAlpha:
            return name 
def check_password():
    pas     =   input("Please enter password:\n")
    isDigit =   False
    isAlpha =   False
    if 4<=len(pas)<=8:
        for _ in pas:
            if _.isdigit():
                isDigit=True
            if _.isalpha():
                isAlpha=True
        if isDigit and isAlpha:
            return pas
    else:
        pass
        
def registerUser(friends):
    ch_username=check_username(friends)
    if ch_username==None:
        print("Username not valid\n")
        
    else:
        ch_pas=check_password()
        if ch_pas==None:
            print("Password not valid\n")
        else:
          friends[ch_username]=ch_pas+'-'
            
def Login(friends):
    username        =   input("Please enter username:\n")
    password        =   input("Please enter password:\n")
    if username in friends.keys():
        if password == friends[username].split("-")[0]:
            print("Logged in\n")
            return username
        else:
            print("Wrong password or username\n")
    else:
        print("Wrong password or username\n")
        
def addFriend(username,friends):
    if username=="":
        print("You need to log in first\n")
    else:
        add_friend=input("Please enter the name of your new friend:\n")
        if add_friend in friends.keys():
          if ',' in friends[username]:
            friends[username]=friends[username]+','+add_friend
          else:
            friends[username]=friends[username]+add_friend
        else:
            print("Friend not found\n")
               
def showFriends(username,friends):
    if username=="":
        print("You need to log in first\n")
    else:
        newfriends=str(friends[username].split("-")[1])
        print(newfriends)
        
def menu():
    menu_text=int(input("1. Log in / change user\n2. Create new user\n3. Add friend\n4. Show my friends\n5. Exit\n"))
    return menu_text

def main():
    while True:
        global friends
        menu_text=menu()
        if menu_text==1:
            global logged_user
            logged_user=Login(friends)
        elif menu_text==2:
            registerUser(friends)
        elif menu_text==3:
            if logged_user==None:
                pass
            else:
                addFriend(logged_user,friends)
        elif menu_text==4:
            if logged_user==None:
                pass
            else:
                showFriends(logged_user,friends)
        elif menu_text==5:
            exitt(friends)
        else:
            print("Invalid option\n")
main()
