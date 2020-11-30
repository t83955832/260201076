eq1,eq2=input("Enter the first equation:\n"),input("Enter the second equation:\n")
newEquation1=eq1.split("=")[0]+eq1.split("=")[1].replace("-","_").replace("+","-").replace("_","+")
newEquation2=eq2.split("=")[0]+eq2.split("=")[1].replace("-","_").replace("+","-").replace("_","+")
splittedList,splittedList2,newItem,newItem2 = [],[],"",""
for i in range(len(newEquation1)):
    if newEquation1[i] in ["+","-"]:
        if newItem != "": splittedList.append(newItem)
        newItem = ""
        newItem += newEquation1[i]  # if you want to include the delimiter
    else: newItem += newEquation1[i]
if newItem != "": splittedList.append(newItem)  # add the last item to output list
for i in range(len(newEquation2)):
    if newEquation2[i] in ["+","-"]:
        if newItem2 != "": splittedList2.append(newItem2)
        newItem2 = ""
        newItem2 += newEquation2[i]  # if you want to include the delimiter
    else: newItem2 += newEquation2[i]
if newItem2 != "": splittedList2.append(newItem2)  
a,b,c,d,e,f = 0,0,0,0,0,0
for item in splittedList:
    if item[-1] == "x": a += int(item[:-1])
    elif item[-1] == "y": b += int(item[:-1])
    else: c += int(item)
print("Equations in the simplified form:")
if b < 0:print(str(a)+"x"+str(b)+"y"+"="+str(-c))
else:print(str(a)+"x"+"+"+str(b)+"y"+"="+str(-c))
for item in splittedList2:
    if item[-1] == "x": d += int(item[:-1])
    elif item[-1] == "y": e += int(item[:-1])
    else: f +=int(item)
if e < 0:print(str(d)+"x"+str(e)+"y"+"="+str(-f))
else:print(str(d)+"x"+"+"+str(e)+"y"+"="+str(-f))
c*=-1
f*=-1
a_divide_d=-(a/d)
last_eq_c=c+(a_divide_d)*f 
last_eq_b=b+(a_divide_d)*e 
result_y=last_eq_c/last_eq_b
result_x=(c-(b*result_y))/a
print("Solution:")
print("x="+str(int(result_x))+"\n"+"y="+str(int(result_y)))