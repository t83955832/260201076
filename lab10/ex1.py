
def multi(number):
    if number==1:
        return 3
    else:
        return 3+multi(number-1)

number=int(input("Please enter an integer : "))

print(multi(number))