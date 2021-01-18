def findstep(arr): 

    lenghtofarr=len(arr)
    counter = 0
    for x in range(lenghtofarr): 
        for y in range(x + 1, lenghtofarr): 
            if (arr[x] > arr[y]): 
                counter += 1
  
    return counter 

arr = [13, 1, 27, 33, 14, 26, 72, 48, 16, 15, 6, 64, 79, 3, 39, 73, 93, 68, 41, 87, 28, 97,
67, 20, 29, 9, 12, 94, 94, 96, 88, 69, 49, 78, 91, 2, 47, 87, 29, 79, 18, 55, 88, 67,
37, 26, 51, 84, 85, 7, 84, 96, 91, 16, 28, 45, 98, 11, 92, 43, 59, 31, 58, 39, 76, 45,
26, 57, 52, 40, 82, 54, 94, 96, 4, 76, 6, 2, 44, 79, 56, 19, 71, 62, 10, 79, 86, 98,
5, 13, 5, 37, 17, 74, 75, 43, 46, 51, 94, 38, 30, 13, 5, 94, 4, 22, 6, 44, 40, 53, 69,
88, 41, 2, 54, 50, 21, 68, 81, 69]


myset=set(arr)
print(len(arr)-len(myset))
x=list(myset)
print("Required Step:",findstep(arr))