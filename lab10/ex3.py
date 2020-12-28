a_list = [3,12,76,[4,56,43],[2,8],81,75]

def sumOfList(n):
    counter=0
    for i in n:
        if type(i) != type([]):
            counter+=i
        else:
            counter+=sumOfList(i)
    return counter
print(sumOfList(a_list))