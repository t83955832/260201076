

def primeNumber(num1,num2):
    if num1>1 and num2>1:
        for i in range(2,num1):
            if num1%i==0:
                print(num1,"is not a prime number")
                break
            else:
                print(num1,"is a prime number")
        for x in range(2,num2):
            if num2%x==0:
                print(num2,'is not a prime number')
                break
            else:
                print(num2,"is a prime number")
    else:
        print(num1,num2,"is not a prime number")
        






num1 = int(input("Enter first number"))
num2=int(input("Enter second number"))
print(primeNumber(num1,num2))