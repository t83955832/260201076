#260201076

#(fp) -> MEANS (FOOT/PEGASUS) 
#travel -> MEANS TASKS NAME in TaskList.txt (Task1,Task2,Task3,Task4,Task5) when user entered.

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

    #WELCOME THE GAME BOARD THAT First of all , THE USER WİLL SEE THESE.Then the user will choose given options by program.
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
        # If only 1 person finished the game, then the block of code that will print their information so far
        first       =   names[hours.index(sortedHours[0])]+","+str(sortedHours[0])#ONLY NAME AND HOURS OF THE FİRST USER

        return [first]

    elif len(names)==2:
        #If only 2 person finished the game, then the block of code that will print their information so far
        first       =   names[hours.index(sortedHours[0])]+","+str(sortedHours[0])# NAME AND HOURS OF THE FİRST USER
        del names[hours.index(sortedHours[0])]
        hours.remove(sortedHours[0])

        second      =   names[hours.index(sortedHours[1])]+","+str(sortedHours[1])# NAME AND HOURS OF THE SECOND USER

        return [first,second]
    else:
        #If only 3 person finished the game, then the block of code that will print their information so far
        first       =   names[hours.index(sortedHours[0])]+","+str(sortedHours[0])#NAME AND HOURS OF THE FİRST USER
        del names[hours.index(sortedHours[0])]
        hours.remove(sortedHours[0])

        second      =   names[hours.index(sortedHours[1])]+","+str(sortedHours[1])#NAME AND HOURS OF THE SECOND USER
        del names[hours.index(sortedHours[1])]
        hours.remove(sortedHours[1])

        third       =   names[hours.index(sortedHours[2])]+","+str(sortedHours[2])#NAME AND HOURS OF THE THIRD USER

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
        exit()#if the user do all the tasks , the user will win the game successfully then the program ends successfully. 

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
                #The part that controls whether the names of the tasks given in the tasklist are entered except of the names.
              print("Invalid input")

        while True:     

          fp=input("How do you want to travel?(Foot/Pegasus)").capitalize()

          if taskList[index][1]==-1 and fp in("Foot"):
              # According to data of TaskList.txt , the user wants to go to tasks by foot ,but defined in tasklist (-1).Therefore, the user does not go to tasks by foot.
              print("You cannot go there by foot.")

          elif fp not in("Pegasus","Foot"):
              # when the user entered except pegasus or foot , because the user should go to by foot or pegasus
              print("Invalid input")


          else:
              if fp=="Pegasus":
                  mytime=int(taskList[index][2]/pegasus)

                  if mytime*pegasuslose<hpOfPegasus:

                      hpOfHero=int(hpOfHero-taskList[index][3])# hero attack the monster then hero lose some hp
                      hpOfPegasus=hpOfPegasus-mytime*pegasuslose # goes to task by pegasus then pegasus lose some hp
                      timer+=mytime # The block that keeps the total time the user has done on tasks.



                      print("Hero defeated the monster.")#after the hero goes to defination tasks, hero attacks the monster 
                      print("Time passed :",(timer),"hour\n")#passed total time
                      print("Remaining HP for Hero :",hpOfHero)#Following hero attacks the monster , remaining hp of hero
                      print("Remaining HP for Pegasus:",hpOfPegasus,"\n")#after the travel by pegasus , remaining hp of pegasus
                      
                      while True:
                          #back home
                          goHome=input("How do you want to go home?(Foot/Pegasus)").capitalize()

                          if goHome not in("Pegasus","Foot"):
                              # when entered except that pegasus or foot
                              print("Invalid input")

                          else:
                              #when back home , the user enter pegasus to back home 
                              if goHome=="Pegasus":
                                  #back home by pegasus
                                  mytime=int(taskList[index][2]/pegasus)

                                  if mytime*pegasuslose<hpOfPegasus:
                                      hpOfPegasus=hpOfPegasus-mytime*pegasuslose
                                      timer+=mytime# The block that keeps the total time the user has done on tasks.

                                      
                                      print("Hero arrived home.")#hero goes home
                                      print("Time passed:",timer,"hour\n")#passed total time
                                      print("Remaining HP for Hero :",hpOfHero)# after the tasks , remaining hp of hero
                                      print("Remaining HP for Pegasus:",hpOfPegasus,"\n")#after the travel, remaining hp of pegasus
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
                                  ## According to data of TaskList.txt , the user wants to go to tasks by foot ,but defined in tasklist (-1).Therefore, the user didn't go to tasks by foot.
                                  print("You cannot go there by foot.")

                              elif goHome=="Foot":
                                  #back home by foot
                                  mytime=int(taskList[index][1]/walking)#hero attack the monster then lose some hp
                                  hpOfHero=hpOfHero-mytime*walkinglose# hero goes to task by foot then lose some hp 
                                  timer+=mytime# The block that keeps the total time the user has done on tasks.


                                  if hpOfHero<0:

                                      print("Hero does not enough HP")
                                      print("Game Over.")
                                      exit()

                                  print("Hero arrived home.")#hero goes home
                                  print("Time passed:",timer,"hour\n")# passed total time
                                  print("Remaining HP for Hero :",hpOfHero)#after the task , remaining hp of hero
                                  print("Remaining HP for Pegasus:",hpOfPegasus,"\n")#after the travel , remaining hp of pegasus
                                  return travel,hpOfPegasus,hpOfHero,timer

                              else:
                                pass                
                  else:

                    print("Pegasus does not have enough HP.")

                    if travel in ("Task1","Task2"):
                        #If the remaining missions are not going by foot and Pegasus has no enough hp, the block to finish the game.
                      print("Game Over")
                      exit()

                    else:pass     
                      
              elif fp=="Foot":
                  # the user goes to task by foot

                  mytime=int(taskList[index][1]/walking)
                  hpOfHero=int(hpOfHero-taskList[index][3])#hero lose some hp who attacks the monster
                  hpOfHero=hpOfHero-mytime*walkinglose# hero goes to tasks by foot who lose some hp
                  timer+=mytime# The block that keeps the total time the user has done on tasks.

                  if hpOfHero<0:

                    print("Hero does not enough HP")
                    print("Game over")
                    exit()

                  print("Hero defeated the monster.")#hero attacks the monster
                  print("Time passed :",(timer),"hour\n")#passed total time
                  print("Remaining HP for Hero :",hpOfHero)#after the hero attacks the monster, remaining hp of hero
                  print("Remaining HP for Pegasus:",hpOfPegasus,"\n")#after the travel by pegasus , remaining hp of pegasus

                  while True:
                      #back home input
                      goHome=input("How do you want to go home?(Foot/Pegasus)").capitalize()

                      if goHome not in("Pegasus","Foot"):
                          # when the user entered except pegasus or foot , because the user should go to by foot or pegasus
                          print("Invalid input")

                      else:

                          if goHome=="Pegasus":
                              # the user wants to back home by pegasus 
                              mytime=int(taskList[index][2]/pegasus)

                              if mytime*pegasuslose<hpOfPegasus:

                                  hpOfPegasus=hpOfPegasus-mytime*pegasuslose# According to data of TaskLists,pegasus goes to tasks,so it loses some hp 
                                  timer+=mytime# The block that keeps the total time the user has done on tasks.

                                  if len(taskList)==1:

                                      print("Hero arrived home.")#hero goes  home
                                      print("Time passed",timer,"hours\n")#total time
                                      return travel,hpOfPegasus,hpOfHero,timer

                                  else:

                                    print("Hero arrived home.") # hero goes home
                                    print("Time passed:",timer,"hour\n")#passed total time
                                    print("Remaining HP for Hero :",hpOfHero)   # after the task , remaining hp of hero
                                    print("Remaining HP for Pegasus:",hpOfPegasus,"\n") #after the travel,remaining hp of pegasus
                                    return travel,hpOfPegasus,hpOfHero,timer

                              else:

                                  print("Pegasus does not have enough HP.")
                                  if travel in ("Task1","Task2"):
                                      #If the remaining missions are not going by foot and Pegasus has no enough hp, the block to finish the game.
                                    print("Game Over")
                                    exit()

                                  else:pass

                          elif taskList[index][1]==-1 and goHome in("Foot"):
                            # According to data of TaskList.txt , the user wants to go to tasks by foot ,but defined in tasklist (-1).Therefore, the user didn't go to tasks by foot.
                              print("You cannot go there by foot.")

                          elif goHome=="Foot":
                              
                              mytime=int(taskList[index][1]/walking)
                              hpOfHero=hpOfHero-mytime*walkinglose
                              timer+=mytime# The block that keeps the total time the user has done on tasks.

                              if hpOfHero<0:

                                  print("Hero does not enough HP")
                                  print("Game over")
                                  exit()

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
    
    printRemainingTasks(taskList)#when the user finish  the tasks , that function will be executed
    
    myprinter3()                

    completedTask,hpOfPegasus,hpOfHero,timer =   main(taskList,hpOfPegasus,hpOfHero,timer)#It is a block of code that redirects to a function named main that maintains the functioning of the program.

    taskList      =   removeTask(taskList,completedTask,newTaskList)#The code block that sends the tasks to the function named remove Task from the total tasks we have as the user performs tasks.

    Congrulations(taskList,timer)#When the user finish the game , that function will be executed
    myprinter2()

