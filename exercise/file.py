f_path=open("ticket.txt","r")
lines=f_path.readlines()
lines="".join(lines).split(";")
newlines=[]
for x in lines:
    newlines.append(x.replace("\n",""))

print(newlines)
