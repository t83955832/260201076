#260201076

hpOfHero    =   3000 # hero has 3000 hp 
hpOfPegasus =   550 # pegasus of hero has 550 hp
#these are will decrease during game.
timer       =   0  

def file():
    #The part where I read the given text file and throw it to the variable
    file        =   open("TaskList.txt","r") # I read here on TaskList.
    taskList    =   []
    myList      =   []

    # The part where each of the rows in the text file is thrown to the variable.
    for _ in file:
        myList  =   [_.split(",")[0],int(_.split(",")[1]),int(_.split(",")[2]),int(_.split(",")[3].replace("\n",""))]
        taskList.append(myList)
        myList  =   []   

    #Since I have to use it in other functions, I open it with return.
    return taskList

taskList    =   file()#to use another function ı took as global variable
newTaskList =   taskList

def myprinter(hpOfHero,hpOfPegasus):

    #WELCOME THE GAME BOARD THAT First of all , THE USER WİLL SEE THESE
    print("Welcome to Hero’s 5 Labors!")
    print("Remaining HP for Hero :",hpOfHero)
    print("Remaining HP for Pegasus:",hpOfPegasus)
    print("Here are the tasks left that hero needs to complete:")
    print("----------------------------------------------------")
    print("|TaskName\t| ByFootDistance| ByPegasus | HPNeeded |")
    print("----------------------------------------------------")

# I have to show the menu to the user because the user needs to know what to choose.
myprinter(hpOfHero,hpOfPegasus)

def removeTask(taskList,travel,newTaskList):
   
    if travel == taskList[0][0]:
        newTaskList.remove(taskList[0])#block of code that removes the task done by the user from the menu
        return newTaskList
    else:
         #I delete whatever task the user has finished and show the remaining tasks to the user again.
        return removeTask(taskList[1:],travel,newTaskList)

def printRemainingTasks(taskList):
    if len(taskList)==0:
        pass
    else:
        #Here is the piece that shows the features and names of the tasks
        print("| "+taskList[0][0]+" \t|",taskList[0][1],"km"+"  \t\t|",taskList[0][2],"km"+"  \t|",taskList[0][3]," \t   |")
        return printRemainingTasks(taskList[1:])


def createFile(name,timer):
    #The block that creates the text file of the halloffame list when the user finishes the game and enters users name
    file    =   open("HallOfFame.txt","a+")
    mystr   =   name+","+str(timer)+"\n"
    #here ı wrote user name by user entered in HallOfFame.txt
    file.write(mystr)

def readAndSortFile():
    #sorting block for the name and duration of the user who read the data from the created halloffame list and made the best 3 timings
    file                    =   open("HallOfFame.txt","r+")
    names,hours,sortedHours =   [],[],[]

    
    for x in file:
        names.append(x.split(",")[0])#read name in the halloffame.txt
        hours.append(x.split(",")[1].replace("\n",""))#read hours of name in the halloffame.txt

    sortedHours     =   list(map(int,sortedHours))#convert to int
    hours           =   list(map(int,hours))#convert to int
    sortedHours     =   sorted((hours))[0:3]#best of three 

    if len(names)==1:

        first       =   names[hours.index(sortedHours[0])]+","+str(sortedHours[0])

        return [first]

    elif len(names)==2:

        first       =   names[hours.index(sortedHours[0])]+","+str(sortedHours[0])
        del names[hours.index(sortedHours[0])]
        hours.remove(sortedHours[0])

        second      =   names[hours.index(sortedHours[1])]+","+str(sortedHours[1])

        return [first,second]
    else:

        first       =   names[hours.index(sortedHours[0])]+","+str(sortedHours[0])
        del names[hours.index(sortedHours[0])]
        hours.remove(sortedHours[0])

        second      =   names[hours.index(sortedHours[1])]+","+str(sortedHours[1])
        del names[hours.index(sortedHours[1])]
        hours.remove(sortedHours[1])

        third       =   names[hours.index(sortedHours[2])]+","+str(sortedHours[2])

        return [first,second,third]

def Congrulations(taskList,timer):
    
    if len(taskList)==0:
        #code block that gets the name of the user when the game is finished
        print("Congratulations, you have completed the task.")
        name=input("What is your name : ").capitalize()
        createFile(name,timer)
        halloflist=readAndSortFile()
        print("Hall of fame")
        print("--------------------------")
        print("| Name\t\t|Finish Time |")
        print("--------------------------")

        for n in halloflist:
            print("| "+n.split(",")[0]+"\t\t|"+n.split(",")[1]+"hour\t|")
            print("--------------------------")
        exit()#the program finish there successfully

    else:
        pass


def main(taskList,hpOfPegasus,hpOfHero,timer):
    pegasus=50#The pegasus can fly at the speed
    pegasuslose=15#the pegasus loses /hour
    walking=20#The hero can walk at the speed
    walkinglose=10#the hero loses /hour
    mytime=0#total_time

    while True:
        #CHECKİNG NAME OF TASK
        verifyString=""
        while verifyString=="":            
            travel=input("Where should Hero go next?").capitalize()
            index=0
            for z in taskList:
                if travel in z:
                    index=taskList.index(z)
                    verifyString=travel
                else:
                    pass    
            if verifyString=="":
              print("Invalid input")

        while True:     

          fp=input("How do you want to travel?(Foot/Pegasus)").capitalize()

          if taskList[index][1]==-1 and fp in("Foot"):
              print("You cannot go there by foot.")

          elif fp not in("Pegasus","Foot"):
              print("Invalid input")


          else:
              if fp=="Pegasus":
                  mytime=int(taskList[index][2]/pegasus)

                  if mytime*pegasuslose<hpOfPegasus:

                      hpOfHero=int(hpOfHero-taskList[index][3])
                      hpOfPegasus=hpOfPegasus-mytime*pegasuslose
                      timer+=mytime # The block that keeps the total time the user has done on tasks.

                      if mytime*walkinglose+int(taskList[index][3])>hpOfHero:
                          print("Hero does not enough HP")
                          print("Game Over")
                          exit()

                      print("Hero defeated the monster.")
                      print("Time passed :",(timer),"hour\n")
                      print("Remaining HP for Hero :",hpOfHero)
                      print("Remaining HP for Pegasus:",hpOfPegasus,"\n")
                      
                      while True:
                          goHome=input("How do you want to go home?(Foot/Pegasus)").capitalize()
                          if goHome not in("Pegasus","Foot"):
                              print("Invalid input")
                          else:
                              if goHome=="Pegasus":
                                  mytime=int(taskList[index][2]/pegasus)
                                  if mytime*pegasuslose<hpOfPegasus:
                                      hpOfPegasus=hpOfPegasus-mytime*pegasuslose
                                      timer+=mytime# The block that keeps the total time the user has done on tasks.
                                      if mytime*walkinglose+int(taskList[index][3])>hpOfHero:
                                          print("Hero does not enough hp")
                                          print("Game Over")
                                          exit()
                                      
                                      print("Hero arrived home.")
                                      print("Time passed:",timer,"hour\n")
                                      print("Remaining HP for Hero :",hpOfHero)
                                      print("Remaining HP for Pegasus:",hpOfPegasus,"\n")
                                      return travel,hpOfPegasus,hpOfHero,timer
                                  else:
                                      print("Pegasus does not have enough HP.")
                                      if travel in ("Task1","Task2"):
                                          #If the remaining missions are not going by foot and Pegasus has no enough hp, the block to finish the game.
                                          print("Game Over")
                                          exit()
                                      else:
                                        pass    
                                      
                                      
                              elif taskList[index][1]==-1 and goHome in("Foot"):
                                  print("You cannot go there by foot.")
                              elif goHome=="Foot":
                                  mytime=int(taskList[index][1]/walking)
                                  hpOfHero=hpOfHero-mytime*walkinglose
                                  timer+=mytime# The block that keeps the total time the user has done on tasks.
                                  if mytime*walkinglose+int(taskList[index][3])>hpOfHero:
                                      print("Hero does not enough hp")
                                      print("Game over")
                                      exit()

                                  print("Hero arrived home.")
                                  print("Time passed:",timer,"hour\n")
                                  print("Remaining HP for Hero :",hpOfHero)
                                  print("Remaining HP for Pegasus:",hpOfPegasus,"\n")
                                  return travel,hpOfPegasus,hpOfHero,timer
                              else:
                                pass                
                  else:
                    print("Pegasus does not have enough HP.")
                    if travel in ("Task1","Task2"):
                        #If the remaining missions are not going by foot and Pegasus has no enough hp, the block to finish the game.
                      print("Game Over")
                      exit()
                    else:
                      pass    
                      
              elif fp=="Foot":
                  mytime=int(taskList[index][1]/walking)
                  hpOfHero=int(hpOfHero-taskList[index][3])
                  hpOfHero=hpOfHero-mytime*walkinglose
                  timer+=mytime# The block that keeps the total time the user has done on tasks.
                  print("Hero defeated the monster.")
                  print("Time passed :",(timer),"hour\n")
                  print("Remaining HP for Hero :",hpOfHero)
                  print("Remaining HP for Pegasus:",hpOfPegasus,"\n")
                  while True:
                      goHome=input("How do you want to go home?(Foot/Pegasus)").capitalize()
                      if goHome not in("Pegasus","Foot"):
                          print("Invalid input")
                      else:
                          if goHome=="Pegasus":
                              mytime=int(taskList[index][2]/pegasus)
                              if mytime*pegasuslose<hpOfPegasus:
                                  hpOfPegasus=hpOfPegasus-mytime*pegasuslose
                                  timer+=mytime# The block that keeps the total time the user has done on tasks.
                                  if len(taskList)==1:
                                      print("Hero arrived home.")
                                      print("Time passed",timer,"hours\n")
                                      return travel,hpOfPegasus,hpOfHero,timer
                                  else:
                                    print("Hero arrived home.")
                                    print("Time passed:",timer,"hour\n")
                                    print("Remaining HP for Hero :",hpOfHero)
                                    print("Remaining HP for Pegasus:",hpOfPegasus,"\n")
                                    return travel,hpOfPegasus,hpOfHero,timer
                              else:
                                  print("Pegasus does not have enough HP.")
                                  if travel in ("Task1","Task2"):
                                      #If the remaining missions are not going by foot and Pegasus has no enough hp, the block to finish the game.
                                    print("Game Over")
                                    exit()
                                  else:
                                    pass  

                          elif taskList[index][1]==-1 and goHome in("Foot"):
                              print("You cannot go there by foot.")
                          elif goHome=="Foot":
                              mytime=int(taskList[index][1]/walking)
                              hpOfHero=hpOfHero-mytime*walkinglose
                              timer+=mytime# The block that keeps the total time the user has done on tasks.
                              if len(taskList)==1:
                                  print("Hero arrived home.")
                                  print("Time passed:",timer,"hour\n")
                                  return travel,hpOfPegasus,hpOfHero,timer
                              else: 
                                print("Hero arrived home.")
                                print("Time passed:",timer,"hour\n")
                                print("Remaining HP for Hero :",hpOfHero)
                                print("Remaining HP for Pegasus:",hpOfPegasus,"\n")
                                return travel,hpOfPegasus,hpOfHero,timer
                          else:
                              pass

def myprinter2():
    #complementary parts to other menu shown while the program is running
  print("Here are the tasks left that hero needs to complete:")
  print("| TaskName | ByFootDistance | ByPegasus | HPNeeded |")
  print("----------------------------------------------------")

def myprinter3():
    #complementary parts to other menu shown while the program is running
 print("----------------------------------------------------\n")

while True:
    printRemainingTasks(taskList)
    myprinter3()                
    completedTask,hpOfPegasus,hpOfHero,timer =   main(taskList,hpOfPegasus,hpOfHero,timer)
    taskList      =   removeTask(taskList,completedTask,newTaskList)
    Congrulations(taskList,timer)
    myprinter2()