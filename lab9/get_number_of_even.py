
numbers=[0,1,2,3,4,5]
def rec(l):
    counter=0
    for _ in l:
        if _%2==0:
            counter+=1
    return counter
print(rec(numbers))