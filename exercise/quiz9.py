def isAnagram(str1,str2):
    count=0
    for _ in str1:
        for x in str2:
            if _==x:
                count=count+1
            else:pass
    if count==len(str1):
        return print("anagram")
    else:
        return print("not anagram")

str1=input("string 1:")
str2=input("string 2:")
isAnagram(str1,str2)