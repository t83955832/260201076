input1 = input("GARDAŞ INPUT'U ALAYIM:   ")
print("input:\n"+input1)
#1 - collect everything to left, with changing the sign
part1 = input1.split("=")[0]
part2 = input1.split("=")[1].replace("-","_").replace("+","-").replace("_","+")
leftSidedForm = part1+part2
#2 - Split with multiple delimiters
splittedList = []
newItem = ""
for i in range(len(leftSidedForm)):
    if leftSidedForm[i] in ["+","-"]:
        if newItem != "": splittedList.append(newItem)
        newItem = ""
        newItem += leftSidedForm[i]  # if you want to include the delimiter
    else: newItem += leftSidedForm[i]
if newItem != "": splittedList.append(newItem)  # add the last item to output list
print("\nSplitted list:")
print(splittedList)

#3 - Grouping Xs, Ys and Constants and Create Summary
a,b,c,d,e,f = 0,0,0,0,0,0
for item in splittedList:
    if item[-1] == "x": a += int(item[:-1])
    elif item[-1] == "y": b += int(item[:-1])
    else: c += int(item)
print("\nSummary:")
if b < 0: print("{}x{}y={}".format(a,b,-c))
else: print("{}x+{}y={}".format(a,b,-c))
