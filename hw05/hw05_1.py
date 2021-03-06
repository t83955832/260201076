import random

class Gamebot:

    def __init__(self, play_hand, stack):
        self.play_hand = play_hand                  # a reference to the player's hand
        self.stack = stack                          # a reference to the stack
        self.count_deck = [['b',1],['b',1],['b',1],['b',2], # a list to count the remaining
                           ['b',2],['b',3],['b',3],['b',4], # cards in the deck
                           ['w',1],['w',1],['w',1],['w',2],
                           ['w',2],['w',3],['w',3],['w',4]]
        for card in play_hand:                      # bot has already seen the player's hand,so it knows
            self.update_count_deck(card)            # that those cards are not in the deck anymore.
        self.hand = [['!',-1],['!',-1],['!',-1]]    # bot's hand. '!' indicates unknown color,
                                                    # -1 indicates unknown value

    def get_tip(self, tip):

        self.tip        =   tip
        lengthOfTips    =   len(tip.split(","))-1
        locations       =   tip.split(",")[:lengthOfTips]
        myTip           =   str(tip.split(",")[-1])

        

        for x in locations:

            if myTip in ("b","w"):
                self.hand[int(x)-1][0]=myTip
            else: 
                self.hand[int(x)-1][1]=int(myTip)
            

                


        #----------------------------------------------------------------
        # Comments of TA's
        # input: tip: a string entered by the player in the form of "loc1,loc2*,loc3*,tip"
        # where * indicates optionality and tip is either a value or a color.
        # e.g. "1,2,w" or "2,3" or "1,2,3,2"
        # output: none
        # The tip is processed and the information about the bot's hand is updated.
        #-----------------------------------------------------------------

    def update_count_deck(self,card):
        self.count_deck.remove(card)

        #-----------------------------------------------
        #Comments Of TA's
        # input: card to be removed
        # output: none
        # card is removed from the count_deck of the bot.
        #-----------------------------------------------
        

    def update_hand(self,num,lengthOfCompHand):

        lengthOfSelfHand=len(self.hand)

        if lengthOfCompHand ==lengthOfSelfHand:
            self.hand[num-1]=["!",-1]

        else:
            self.hand.pop(num-1)




        #---------------------------------------------------------
        #Comments of TA's
        # input: num: location of the card to be removed from the bot's hand
        # output: none
        # A card is removed from the bot's hand according to the given input and a new one is appended.
        #----------------------------------------------------------


    def give_tip(self):

        playerHand={1:[],2:[],3:[],4:[],"w":[],"b":[]}
        counter=1
        for _ in self.play_hand:
            for x in _:
                playerHand[x].append(counter)
            counter+=1
        
        
        keyOfTip=[k for k in playerHand.keys() if len(playerHand.get(k))==max([len(n) for n in playerHand.values()])][0]
        #print("key of tip : ",playerHand[keyOfTip])
        tipsOfBot=[]
        for i in playerHand[keyOfTip]:
            tipsOfBot.append(str(i))

        tipsOfBot.append(str(keyOfTip))
        
        
        if len(playerHand[keyOfTip])>=3:

            return tipsOfBot[0]+","+tipsOfBot[1]+","+str(tipsOfBot[2])+","+str(tipsOfBot[3])

        else:

            if len(playerHand[keyOfTip])>=2:
                return tipsOfBot[0]+","+str(tipsOfBot[1])+","+str(tipsOfBot[2])

            else:

                if len(playerHand[keyOfTip])>=1:
                    return str(tipsOfBot[0])+","+str(tipsOfBot[1])

                else:
                    pass



        #---------------------------------------------------------------------------------------------
        #Comments of TA's
        # input: none
        # output: a string created by the bot in the form of "loc1,loc2*,loc3*,tip"
        # where * indicates optionality and tip is either a value or a color.
        # e.g. "1,2,w" or "2,3" or "1,2,3,2"
        # The bot checks the player's hand and finds a good tip to give. Minimal requirement for this
        # function is that bot gives the tip for maximum possible number of cards.
        # BONUS: Smarter decision-making algorithms can be implemented.
        #-----------------------------------------------------------------------------------------------

    def pick_stack(self):
        #self.hand = [["b",1],["w",1],["w",2]]
        #stack = [[],[]]
        for x in self.hand:

            if "b" in x:
                if len(self.stack[0])+1==x[1]:
                    return [x[0],x[1]]
                else:
                    pass

            elif "w" in x:
                if len(self.stack[1])+1 ==x[1]:
                    return [x[0],x[1]]
                else:
                    pass
                    
        return -1


        #----------------------------------------------------------------------------------
        #Comments of TA's
        # input: none
        # output: If possible, the location of the card to be placed in the stack, otherwise -1. Minimal
        # the requirement for this function is to find the card to be stacked with 100% certainty.
        # BONUS: Smarter decision-making algorithms can be implemented.
        #----------------------------------------------------------------------------------
        

    def pick_discard(self):
        # REMIND MYSELF !!
        # If the man has more than one of the same cards, discard one.
        #play_hand = [ ["b",1], ["b",1] , ["w",2]] 
        #comp_hand = [ ["b",1] , ["b",1] , ["w",1]] 
        # [["b",1],["b",3],["w",1]]
        # 1
        # ["!",-1] 

        unknown =   ["!",-1]
        for x in self.hand:

            if x in (self.stack[0],self.stack[1]):
                return self.hand.index(x)
            else:
                pass
        
        if unknown in self.hand:
            return self.hand.index(unknown)
            
        else:

            for x in self.hand:
                if unknown[0] in x:
                    return self.hand.index(x)
                elif unknown[1] in x:
                    return self.hand.index(x)
                else:
                    pass
        
            #----
            #for x in self.play_hand:
                #if x in self.hand:
                    #return self.stack.index(x)
                #else:
                    #pass


        #----------------------------------------------------------------------------------
        #Comments of TA's
        # input: none
        # output: The location of the card to be discarded. Minimal requirement for this function is that,
        # if possible, the bot picks the card that is already in the stack. If this is not the case,
        # the bot picks the card of which it has minimum information.
        # BONUS: Smarter decision-making algorithms can be implemented.
        #----------------------------------------------------------------------------------
        

def shuffle(deck):

    lengthOfDeck=len(deck)
    # we define a variable named lengthOfDeck 
    while lengthOfDeck!=0:# As long as the number of elements of the deck is not 0, loop will run.
        
        lengthOfDeck=lengthOfDeck-1
        rnd=random.choice(deck)#this choice method gives us that random element in the deck 
        
        deck.append(rnd)# given elements will be added 
        deck.remove(rnd) # given elements will be removed in the deck 
    
    
    

    #---------------------------
    # Comments of TA's
    # input: deck to be shuffled
    # output: none
    # shuffle the deck
    # you are free to choose the algorithm you want
    # explain your shuffle algorithm in a comment
    #-----------------------------------------------


def print_menu():
    print("Hit 'v' to view the status of the game.")
    print("Hit 't' to spend a tip.")
    print("Hit 's' to try and stack your card.")
    print("Hit 'd' to discard your card and earn a tip.")
    print("Hit 'h' to view this menu.")
    print("Hit 'q' to quit.")

def update_hand(hand,deck,num):

    if len(deck)!=0:

        remCard     =   hand[num-1]
        hand[num-1] =   deck[0]
        deck.remove(deck[0])

    else:
        
        remCard     =   hand[num-1]
        hand.pop(num-1)

    return remCard

    #---------------------------------------------------------------------------------------
    # Comments of TA's
    # input: hand to be updated,current deck and the location of the card to be removed
    # output: removed card
    # This function is called when a card is played (either stacked or discarded). It removes
    # the played card from the hand. If there are any cards left in the deck, the top card
    # in the deck is drawn and appended to the hand.
    #---------------------------------------------------------------------------------------

def try_stack(card,stack,trash,lives):
    #REMİND MYSELF
    #stack [[],[]] 0 means black , 1 means white
    #["b",2]
    #b 2
    #stack = [[1w,2w,3w,4w],[1b,2b,3b,4b]] 
    #strOfCard=" ".join([str(elements) for elements in card])
    if "b" == card[0]:
        #insert the stack[[]]
        
        if len(stack[0])+1==card[1]:

            #strOfCard       =   strOfCard[2]+" "+strOfCard[0]
            stack[0].append(card)
            return lives

            
        else:
            #add to trash
            trash.append(card)
            trash=sorted(trash)
            
            lives=lives-1
            return lives
            
            

    elif "w" == card[0]:
        if len(stack[1])+1==card[1]:
            #i would take card form of w1,w2,w3,w4
            # I change it 1w,2w,3w,4w instead of w1,w2,w3,w4
            #strOfCard       =   strOfCard[2]+" "+strOfCard[0]
            stack[1].append(card)
            return lives

            
        else:
            #add to trash
            trash.append(card)
            trash=sorted(trash)
            
            lives           =   lives-1
            return lives
            
    else:
        pass


    """
    if "b" in card[0]:
        if len(stack[0])!=0:
            for x in stack[0]:
                if card[1]!=stack[0][len(stack[0])-1]:
                    if len(stack[0])>2:
                        if card[1]==stack[0][len(stack[0])-1][1]+1:
                            stack[0].append(card)
                            return lives
                        else:
                            trash.append(card)
                            lives-=1
                            return lives
                    else:
                        if len(stack[0])==2:
                            if card[1]==stack[0][1]+1:
                                stack[0].append(card)
                                return lives
                            else:
                                trash.append(card)
                                lives-=1
                                return lives
                else:
                    trash.append(card)
                    lives-=1
                    return lives
        else:
            if card[1]==1:
                stack[0].append(card)
                return lives
            else:
                trash.append(card)
                lives-=1
                return lives

        

    elif "w" in card[0]:
        if len(stack[1])!=0:
            for x in stack[1]:
                if card[1] != stack[1][len(stack[1])-1]:
                    if len(stack[1])>2:
                        if card[1]==stack[1][len(stack[1])-1][1]+1:
                            stack[1].append(card)
                            return lives
                        else:
                            
                            trash.append(card)
                            lives-=1
                            return lives
                    else:
                        if len(stack[1])==2:
                            if card[1]==stack[1][1]+1:
                                stack[1].append(card)
                                return lives
                            else:
                                trash.append(card)
                                lives-=1
                                return lives
                        
                else:
                    
                    trash.append(card)
                    lives-=1
                    return lives
        else:
            if card[1]==1:
                stack[1].append(card)
                return lives
            else:
                trash.append(card)
                lives-=1
                return lives
    else:
        pass
    """

    #-----------------------------------------------------------------------------
    #Comments of TA's
    # input: the card to be stacked, current stack, current trash, number of lives
    
    # output: updated number of lives
    # This function tries to place the card in the stack. If successful, the card is appropriately
    # added to the stack and the updated stack is printed. Otherwise, the card is appended to the
    # trash, the trash is sorted for better viewing and number of lives is decreased by 1. A warning
    # and the current number of lives are printed.
    #----------------------------------------------------------------------------
    

def discard(card,trash,tips):

    trash.append(play_hand[card-1])
    tips    =   tips+1 
    print(tips)
    trash   =   sorted(trash)
    print(trash)
    return tips



    #-------------------------------------------------------------------
    #Comments of TA's
    # input: the card to be discarded, the current trash, number of tips
    # output: updated number of tips
    # This function appends the card to the trash, re-sorts it and increases the number of tips by 1.
    # The updated trash and the number of tips are printed.
    #-------------------------------------------------------------------

print("Welcome! Let's play!")
print_menu()
deck    = [['b',1],['b',1],['b',1],['b',2],['b',2],['b',3],['b',3],['b',4],
            ['w',1],['w',1],['w',1],['w',2],['w',2],['w',3],['w',3],['w',4]]
stack   = [[],[]] #0 means black, 1 means white
trash   = []
lives   = 2
tips    = 3
shuffle(deck)

# First hands are dealt.
comp_hand =deck[0:3] # TODO: obtain cards (3 cards) from deck
play_hand =deck[3:6] # TODO: obtain cards (3 cards) from deck

del deck[0:6]
bot     = Gamebot(play_hand,stack)  # Gamebot object is created.
turn    = 0                        # 0 means player, 1 means computer. So for each game, the player starts.
while True:
    #print(deck)
    #print("Player Hand : ",play_hand)
    print("Hand of Computer :",comp_hand)
    if turn == 0:
        inp = input("Your turn:")
        if inp == 'v':
            print("Computer's hand:",comp_hand)
            print("Number of tips left:", tips)
            print("Number of lives left:", lives)
            print("Current stack:")
            print("Black:", stack[0])
            print("White:", stack[1])
            trash=sorted(trash)
            print("Current trash:",trash)
        elif inp == "t":
            if tips > 0:
                turn    =   1        # Switch turns.
                tip     =   input("Player gives a tip:\n")
                bot.get_tip(tip)
                tips    =   tips-1
                print("Tips:",tips)

                #--------------------------------
                #Comments of TA's
                # Take a tip from the player, give it to the bot, update and print the number of tips.
                #---------------------------------------

            else:
                print ("Not possible! No tips left!")
        elif inp == "s":
            turn = 1
            
            #1w , 2w , 3w , 4w , #1b,2b,3b,4b
            StackedOrderNumberOfCard=int(input("Player stacks a card:\n"))
            
            returnedLives=try_stack(play_hand[StackedOrderNumberOfCard-1],stack,trash,lives)
            if lives!=returnedLives:
                lives=returnedLives
                update_hand(play_hand,deck,StackedOrderNumberOfCard)
            else:
                update_hand(play_hand,deck,StackedOrderNumberOfCard)

            # Switch turns.
            # Take the location of the card to be stacked from the player,
            # update hands and bot's count_deck and try to stack the selected card.
        elif inp == "d":
            if len(play_hand)!=0:
                turn = 1  
                DiscardedOrderNumberOfCard=int(input("Player discards a card:\n")) 
                tips=discard(DiscardedOrderNumberOfCard,trash,tips)
                update_hand(play_hand,deck,DiscardedOrderNumberOfCard)
                #If there are no more cards to be dealt in the deck and the player has 3 cards , we need to check if any of them are discarded, as the player's hand corrupted.
                if len(deck)!=0:
                    bot.update_count_deck(play_hand[DiscardedOrderNumberOfCard-1])
                else:
                    pass

            else:
                print("Wrong Move")
            
            #----------------------------------------------------------------
            #Comments of TA's
            # Switch turns.
            # Take the location of the card to be discarded from the player,
            # update hands and bot's count_deck and discard the selected card.
            #----------------------------------------------------------------
        elif inp == "h":
            print_menu()
        elif inp == "q":
            break
        else:
            print ("Please enter a valid choice (v,t,s,d,h,q)!")
    else:
        # A minimal strategy of the bot is given.
        # BONUS: Smarter rule sets can be implemented.
        
        if tips > 1 and len(play_hand)>0: 
            
            tipOfBot=bot.give_tip()
            print("Computer gives a tip:\n"+tipOfBot)
            tips=tips-1
            print("Tips:",tips)
            #---------------------------------------------------------------
            #Comments of TA's
            # Take a tip from the bot. Update the number of tips. Print both
            # the given tip by the bot and the updated number of tips.
            #---------------------------------------------------------------
        else:
            
            if len(comp_hand)!=0:
                pickStackOfBot=bot.pick_stack()
                if pickStackOfBot==-1:
                
                    pickDiscardOfBot=bot.pick_discard()
                    tips=tips+1
                    print("Computer discards a card:")
                    x=pickDiscardOfBot+1
                    print(x)
                    trash.append(comp_hand[pickDiscardOfBot])
                    update_hand(comp_hand,deck,x)
                    #As we cannot interfere with the length of self.hand in the class named gamebot, I have to send the length of the hand of the computer to the function named update_hand in the class outside the class.
                    bot.update_hand(x,len(comp_hand))
                    

                else:

                    if "b" in pickStackOfBot:
                        print("Computer stacks a card:")
                        print(comp_hand.index(pickStackOfBot)+1)
                        stack[0].append(pickStackOfBot)
                        update_hand(comp_hand,deck,comp_hand.index(pickStackOfBot)+1)
                        #As we cannot interfere with the length of self.hand in the class named gamebot, I have to send the length of the hand of the computer to the function named update_hand in the class outside the class.
                        bot.update_hand(comp_hand.index(pickStackOfBot)+1,len(comp_hand))
                        

                    elif "w" in pickStackOfBot:
                        print("Computer stacks a card:")
                        print(comp_hand.index(pickStackOfBot)+1)
                        stack[1].append(pickStackOfBot)

                        update_hand(comp_hand,deck,comp_hand.index(pickStackOfBot)+1)
                        #As we cannot interfere with the length of self.hand in the class named gamebot, I have to send the length of the hand of the computer to the function named update_hand in the class outside the class.
                        bot.update_hand(comp_hand.index(pickStackOfBot)+1,len(comp_hand))
                    else:
                        pass
            else:
                print("Wrong Move.")



            # Check if bot can pick a card to stack.
            # If yes, update comp_hand, bot's hand and bot's count_deck and try to stack the selected card.
            # If no, make bot pick a card to discard. Update comp_hand, bot's hand and bot's count_deck
            # and discard the selected card.
        turn = 0        # Switch turns.
    score = sum([len(d) for d in stack])
    if lives==0:
        print("No lives left! Game over!")
        print("Your score is", score)
        break
    if len(comp_hand+play_hand)==0:
        print ("No cards left! Game over!")
        print ("Your score is", score)
        break
    if score == 8:
        print ("Congratulations! You have reached the maximum score!")
        break
