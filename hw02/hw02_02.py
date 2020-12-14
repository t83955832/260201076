departure=input("Departure province:\n").upper()
arrival=input("Arrival province:\n").upper()
travel_type=input("Enter travel type:\n").capitalize()

#print("I am calculating the distance between "+departure+" and "+arrival)

file=open("provinces.txt","r")
provList=[]
name_of_city=[]
loc1=[]
loc2=[]
vehicle=["Car","Motorcycle","Bicycle"]
for i in file:
    i.split(",")
    provList.append(i[0:].replace("\n",""))

for i in provList:
    name_of_city.append(i.split(",")[0])
    loc1.append(i.split(",")[1])
    loc2.append(i.split(",")[2])

while True:
    if departure in name_of_city:
        arrival=input("Arrival province:\n").upper()
        if arrival in name_of_city:
            travel_type=input("Enter travel type:\n").capitalize()
            if travel_type in vehicle:
                if departure==arrival:
                    print("Enter a different province!")
                else:
                    arrival=input("Arrival province:\n").upper()
            else:
                travel_type=input("Enter travel type:\n").capitalize()
        else:
            print("Province not found!")
            arrival=input("Arrival province:\n").upper()
    else:
        print("Province not found!")
        departure=input("Departure province:\n").upper()


#print(name_of_city,loc1,loc2)

#print(provList)





