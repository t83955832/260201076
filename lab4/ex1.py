a=int(input(""))
last_digit=a%10
second_digit=(a%100-last_digit)/10
print(last_digit+second_digit)