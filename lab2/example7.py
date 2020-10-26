getDate=input("Please,enter a date ").split(".")
day,month,year=getDate[0],getDate[1],getDate[2]
newDay  =(int(day))%30+1
newMonth=(int(day)+1)//31+int(month)%12
newYear=(int(month)+1)//12+int(year)
print(newDay,".",newMonth,".",newYear)



