import random

deck = [['b',1],['b',1],['b',1],['b',2],['b',2],['b',3],['b',3],['b',4],
        ['w',1],['w',1],['w',1],['w',2],['w',2],['w',3],['w',3],['w',4]]

del deck[0:6]

def shuffle(deck):
    myDeck=[]# we define a new list named myDeck to add shuffled list
    while len(deck)!=0:# As long as the number of elements of the deck is not 0, loop will run.
        rnd=random.choice(deck)#this choice method gives us that random element in the deck 
        myDeck.append(rnd)# given elements will be added 
        deck.remove(rnd) # given elements will be removed in the deck
    myDeck=deck

shuffle(deck)


    
    


print(shuffle(deck))


