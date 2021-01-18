mylist=["b",1]
newmylist=[]
for i in mylist:
    if type(i) == str:
         newmylist.append(str(i))
    else:
        newmylist.append(str(i))

new="".join(newmylist)
new=sorted(new)
if len(mylist)>=3:
    print("Computer gives a tip:\n"+new[0]+","+new[1]+","+new[2])
else:
    if len(mylist)>=2:
        print("Computer gives a tip:\n"+new[0]+","+new[1])
    else:
        if len(mylist)>=1:
            print("Computer gives a tip:\n"+new[0])
        else:
            pass


        