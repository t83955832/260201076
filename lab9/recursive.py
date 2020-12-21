l = [1,2,3,4]
def rec(l):
    if len(l) == 0:return [] 
    else:return [l.pop()] + rec(l)  


print(rec(l))