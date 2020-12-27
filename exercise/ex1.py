
def file():
    file=open("ticket.txt","r")
    dictOfTicket={}
    arr=[]
    name,password,ticketNumber,travelDate,city,flighTime="","","","","",""

    for _ in file:
        name=_.split(";")[0]
        password=_.split(";")[1]
        ticketNumber=_.split(";")[2]
        travelDate=_.split(";")[3]
        city=_.split(";")[4]
        flighTime=_.split(";")[5].replace("\n","")
        arr.append(name)
        arr.append(password)
        arr.append(ticketNumber)
        arr.append(travelDate)
        arr.append(city)
        arr.append(flighTime)
        dictOfTicket[name]=arr
        arr=[]


    return dictOfTicket

def Login():
    dictOfTicket=file()
    username=input("Please enter username:\n")
    if username in dictOfTicket[username]:
        password=input("Please enter password:\n")
        if password in dictOfTicket[username]:
            print("Logged in\n")
        else:
            print("wrong password or username")
    else:
        pass

Login()
    