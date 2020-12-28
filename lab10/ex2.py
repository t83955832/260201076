def hailstone(n):

    if(n==1):
        print(1) 
        return 
    if(n%2 == 0):
        print(n) 
        hailstone(int(n/2))
        return 
    else: 
        print(n) 
        hailstone(int(n*3) + 1)
        return 

number=int(input("value : "))
print(hailstone(number))