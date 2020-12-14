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
                                print("I am calculating the distance between "+departure+" and "+arrival)
                                x1          =   mydict[departure].split("-")[0]
                                x2          =   mydict[arrival].split("-")[0]
                                y1          =   mydict[departure].split("-")[1]
                                y2          =   mydict[arrival].split("-")[1]
                                dx          =   (float(x2)-float(x1))
                                dy          =   (float(y2)-float(y1))
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
        break
    else:
        print("Province not found!")
        print("Possible province:")
        departure   =   input("Departure province:\n").upper()
file.close()
