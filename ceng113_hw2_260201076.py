departure       =   input("Departure province:\n").upper()
file            =   open("provinces.txt","r")

mydict,loc1,loc2,name,dx,dy,x1,x2,y1,y2 =   {},[],[],"",0,0,0,0,0,0
distance,distance_km,time,hours,minutes =   0,0,0,0,0
vehicles                                =   {"Car":90,"Motorcycle":80,"Bicycle":25}
x,y,distances,closest_cities              =   0,0,{},[]

for i in file:
    name        =   i.split(",")[0]
    loc1        =   i.split(",")[1]
    loc2        =   i.split(",")[2].replace("\n","")
    mydict[name]=   loc1+"-"+loc2

possible_provinces_departure    =   []
possible_provinces_arrival      =   []

while True:
    if departure in mydict.keys():
        while True:
            arrival =   input("Arrival province:\n").upper()
            if arrival in mydict.keys():
                while True:
                    if departure==arrival:
                        print("Enter a different province!")
                        arrival =   input("Arrival province:\n").upper()
                        
                    else:
                        while True:
                            travel_type     =   input("Enter travel type:\n").capitalize()
                            if travel_type in vehicles.keys():
                                print("\nI am calculating the distance between "+departure+" and "+arrival+" ...\n")
                                x1          =   float(mydict[departure].split("-")[0])
                                x2          =   float(mydict[arrival].split("-")[0])
                                y1          =   float(mydict[departure].split("-")[1])
                                y2          =   float(mydict[arrival].split("-")[1])
                                dx          =   (x2)-(x1)
                                dy          =   (y2)-(y1)
                                distance    =   (dx*dx+dy*dy)**0.5
                                distance_km =   distance*100
                                time        =   str(distance_km/vehicles[travel_type])
                                hours       =   time.split(".")[0]
                                minutes     =   time.split(".")[1]
                                minutes     =   (float(time)-float(hours))*60 

                                print("Distance:",round(distance_km,2),"km")

                                print("Approximate travel time with "+travel_type.upper()+":",int(hours),"hours",int(minutes),"minutes")

                                for i in mydict.keys():
                                    x               =   float(mydict[i].split("-")[0])
                                    y               =   float(mydict[i].split("-")[1])
                                    distances[i]    =   ((x1-x)**2+(y1-y)**2)**0.5

                                closest_distances   =   sorted(distances.values())[1:4]
                                for a in closest_distances:
                                    for k in distances.keys():
                                        if a ==distances[k]:
                                            closest_cities.append(k)
                                closest_cities.sort() 
                                print("Recommended places close to "+departure+":"+closest_cities[0]+","+closest_cities[1]+","+closest_cities[2])
                                break
                        break
                break
            else:
                print("Province not found!")
                for z in mydict.keys():
                    if z.startswith(arrival):
                        possible_provinces_arrival.append(z)
                possible_provinces_arrival.sort()
                if len(possible_provinces_arrival)==1:
                    possible_provinces_arrival=str(possible_provinces_arrival)
                    print("Possible province:"+possible_provinces_arrival.replace("'","").replace("[","").replace("]","").replace(" ",""))
                    possible_provinces_arrival=[]
                elif len(possible_provinces_arrival)==0:pass
                else:
                    possible_provinces_arrival=str(possible_provinces_arrival)
                    print("Possible provinces:"+possible_provinces_arrival.replace("'","").replace("[","").replace("]","").replace(" ",""))
                    possible_provinces_arrival=[]
        break
    else:
        print("Province not found!")
        for z in mydict.keys():
            if z.startswith(departure):
                possible_provinces_departure.append(z)
        possible_provinces_departure.sort()
        if len(possible_provinces_departure)==1:
            possible_provinces_departure=str(possible_provinces_departure)
            print("Possible province:"+possible_provinces_departure.replace("'","").replace("[","").replace("]","").replace(" ",""))
            possible_provinces_departure=[]
        elif len(possible_provinces_departure)==0:pass
        else:
            possible_provinces_departure=str(possible_provinces_departure)
            print("Possible provinces:"+possible_provinces_departure.replace("'","").replace("[","").replace("]","").replace(" ",""))
            possible_provinces_departure=[]
        departure   =   input("Departure province:\n").upper()
file.close()
