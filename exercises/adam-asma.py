import random
#You can add the words what you want
myList=["pencil","book","mouse","observe","dog","university","school","lecture","engineer","keyboard","hardware","software"].lower()
#your rights to play the game.
trial = int(input("How many trials do you want ? Expect { 0 }  : "))
point =  100 / trial
#Program chooses a word in list
x=random.randint(0,len(myList)-1)
selectProgram = myList[x]
#print(type(selectProgram))
placesOfWords=len(selectProgram)*"_"
listOfLetters=list(placesOfWords)
converter=""
enteredInputs=[]
#letters of the selected word by Program
print(placesOfWords)
while trial!=0:
    if converter==selectProgram:
        print("Congrulations .  ")
        break
    predictOfUser=input("Please Enter your predict : ").lower()
    if predictOfUser in enteredInputs:
        print("You have already entered that letter / word ")
    elif predictOfUser==selectProgram:
        print("Congrulations !   ")
        break
    elif len(predictOfUser)==1:
        counter=0
        for i in range(len(selectProgram)):
            if predictOfUser == selectProgram[i]:
                counter+=1
                listOfLetters[i]=predictOfUser
        converter="".join(listOfLetters)
        #print(listOfLetters)
        print(converter)
        if counter ==0:
            trial-=1
            print("The letter you input is not found in the selected word.\nTrial : ",trial)
        else:
            pass 
    else:
        print("Your predict is wrong , Please you should write other letter")
        trial-=1
        print("Trial : ",trial)
    enteredInputs.append(predictOfUser)
print("Score : ",trial*point)

        


    
    



