a_list = [3,12,76,[4,56,43],[2,8],81,75]

def sumOfList(n):
    s=0
    for i in n:
        if type(i) != type([]):
            s+=i
        else:
            s+=sumOfList(i)
    return s
print(sumOfList(a_list))