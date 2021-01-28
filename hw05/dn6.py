stack=[[["b",1]],[]]
card=["b",3]
lives=2
trash=[]


if "b" == card[0]:
    #insert the stack[[]]
    
    if len(stack[0])+1==card[1]:

        #strOfCard       =   strOfCard[2]+" "+strOfCard[0]
        stack[0].append(card)

        
    else:
        #add to trash
        trash.append(card)
        trash=sorted(trash)
        
        lives=lives-1
        
        

elif "w" == card[0]:
    if len(stack[1])+1==card[1]:
        #i would take card form of w1,w2,w3,w4
        # I change it 1w,2w,3w,4w instead of w1,w2,w3,w4
        #strOfCard       =   strOfCard[2]+" "+strOfCard[0]
        stack[1].append(card)

        
    else:
        #add to trash
        trash.append(card)
        trash=sorted(trash)
        
        lives           =   lives-1
        
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
                        break
                    else:
                        trash.append(card)
                        lives-=1
                        break
                else:
                    if len(stack[0])==2:
                        if card[1]==stack[0][1]+1:
                            stack[0].append(card)
                            break
                        else:
                            trash.append(card)
                            lives-=1
                            break
            else:
                trash.append(card)
                lives-=1
                break
    else:
        if card[1]==1:
            stack[0].append(card)
        else:
            trash.append(card)
            lives-=1

    

elif "w" in card[0]:
    if len(stack[1])!=0:
        for x in stack[1]:
            if card[1] != stack[1][len(stack[1])-1]:
                if len(stack[1])>2:
                    if card[1]==stack[1][len(stack[1])-1][1]+1:
                        stack[1].append(card)
                        break
                    else:
                        print("trash'e ekleniyor1")
                        trash.append(card)
                        lives-=1
                        break
                else:
                    if len(stack[1])==2:
                        if card[1]==stack[1][1]+1:
                            stack[1].append(card)
                            break
                        else:
                            trash.append(card)
                            lives-=1
                            break
                    
            else:
                print("trash'e ekleniyor2 ")
                trash.append(card)
                lives-=1
                break
    else:
        if card[1]==1:
            stack[1].append(card)
        else:
            trash.append(card)
            lives-=1
"""

print("TRASH: ",trash)
print("STACK : ",stack)
print("LİVES : ",lives)