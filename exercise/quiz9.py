def pairStar(mytxt):
    addstarToMytxt="*"
    if len(mytxt)<2:
        return mytxt

    if mytxt[0]==mytxt[1]:
        return mytxt[0] + addstarToMytxt + pairStar(mytxt[1:])
    else:
        return mytxt[0] + pairStar(mytxt[1:])
        
print(pairStar("hello"))