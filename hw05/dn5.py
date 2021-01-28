trash=[["b",3],["b",2],["w",1],["w",4],["b",1],["w",2],["w",3],["b",4]]

trash=sorted(trash)
for x in range(len(trash)):
    trash[x][0],trash[x][1]=trash[x][1],trash[x][0]


print(trash)





