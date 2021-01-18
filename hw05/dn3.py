
deck=[['b',1],['b',1],['b',1],['b',2], 
            ['b',2],['b',3],['b',3],['b',4],
            ['w',1],['w',1],['w',1],['w',2],
            ['w',2],['w',3],['w',3],['w',4]]

comp_hand=[["b",1],["b",3],["w",4]]

play_hand=deck[0:3]

print("player hand : ",play_hand)
print("computer hand : ",comp_hand)

new_comp_hand=str(comp_hand[0][1])+" "+str(comp_hand[0][0])
del deck[0:6]
print(deck)
trash=["1 b"]
stack=[['1 b',"2 b"],['1 w']]

tips=3
if tips==0:
    print("var trash'e yükleneceksin")
    x=(comp_hand[0][0])+" "+str(comp_hand[0][1])
    print(x)
    tips+=1
for x in stack:

    if new_comp_hand in x:
        

        #print(comp_hand.index(x))

        trash.append(new_comp_hand)
        print(trash)
        
        break
    else:
        print("yok peki sıralama yapıp stack yapıcam")


