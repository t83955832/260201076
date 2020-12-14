#print("I am calculating the distance between "+departure+" and "+arrival)


if departure in name_of_city:
        if arrival in name_of_city:
            if departure==arrival:
                print("Enter a different province!")
            else:
                arrival=input("Arrival province:\n").upper()
        else:
            print("Province not found!")
            arrival=input("Arrival province:\n").upper()
    else:
        print("Province not found!")
        departure=input("Departure province:\n").upper()