def rec(l,counter):
    if len(l)==0:
        return counter
    elif l[0]%2==1:
        return rec(l[1:],counter)
    else:
        counter+=1
        return rec(l[1:],counter)
        
numbers=[0,1,2,3,4,5]
counter=0
print(rec(numbers,counter))