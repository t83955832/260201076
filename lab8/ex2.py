def is_prime(n):
    if n<=1:
        return False
    for x in range(2,n):
        if n%x==0:
            return False
    return True
def primesBetween(n,m):
    for x in range(n,m):
        if is_prime(x):
            print(x)
num1=int(input("number1 : "))
num2=int(input("number2 : "))
print(primesBetween(num1,num2))