a=int(input())
b=int(input())
power=1
if b>0:
   for i in range(0,b,1):
       power*=a

else:
    for i in range(0,b,-1):
        power/=a

print(power)
