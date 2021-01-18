play_hand=[["b",4],["b",3],["w",4]]
#4 b
#3 b
#2 w
#computer gives a tip : 1,2,b

        #print(sum([len(_) for _ in play_hand])-sum([len(_) for _ in play_hand if "b" in _ ]))
playerhand={1:[],2:[],3:[],4:[],"w":[],"b":[]}

counter=1

for _ in play_hand:
    for x in _:
        playerhand[x].append(counter)
    counter+=1

print(playerhand)

#yıldız


print(playerhand[keyOfTip])


    
    
    
    
"""
    if "b" in _:
        b=_[:]
        playerhand["b"].append(b)

    if "w" in _:
        w=([len(_) for _ in play_hand if "w" in _])

    if "w" in _:
        playerhand["w"].append("w")
    if "b" in _:
        playerhand["b"].append("b")
    if 1 in _:
        playerhand[1].append(1)
    if 2 in _:
        playerhand[2].append(2)
    if 3 in _:
        playerhand[3].append(3)
    if 4 in _:
        playerhand[4].append(4)
"""



