#userName=input("Enter your username : ")
#userPassword=input("Enter your password : ")
counter = 0
usersFile=open("users.txt","r")
listOfUsers=[]
for users in usersFile:
    listOfUsers.append(users.split(":"))
    listOfUsers[counter][4]=listOfUsers[counter][4][:-2]
    counter+=1

print(listOfUsers)









userName=input("Enter your username : ")
userPassword=input("Enter your password : ")
counter = 0
usersFile=open("users.txt","r")
products_file=open('products.txt','r')

dict_of_users={}
list_of_products=[]
dict_of_products_id={}
listOfUsers=[]

for users in usersFile:
  listOfUsers.append(users.split(":"))
  listOfUsers[counter][3]=listOfUsers[counter][3][:-1]
  dict_of_users[listOfUsers[counter][1]]=listOfUsers[counter][2]
  counter+=1

counter=0
for products in  products_file:
  dict_of_products_name_price={}
  list_of_products.append(products.split(':'))
  list_of_products[counter][2]=list_of_products[counter][2][:-1]
  dict_of_products_name_price[list_of_products[counter][1]]=list_of_products[counter][2]
  dict_of_products_id[list_of_products[counter][0]]=dict_of_products_name_price
  del dict_of_products_name_price

  counter+=1




if userName in dict_of_users.keys():
  if userPassword==dict_of_users[userName]:
    print(dict_of_products_id)
    chosen_id=input('almak istediğiniz ürünün numarasını giriniz')
    




    print('true')
  else:
    print('yanlış')  
else:
  print('yanlış')