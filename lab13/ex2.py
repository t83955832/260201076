def b_search(arr, zero, lenghtOfArr, mynum): 
  
    while zero <= lenghtOfArr: 
  
        middle = zero + (lenghtOfArr - zero) // 2; 
          
        if arr[middle] == mynum: 
            return middle 
        else:
            if arr[middle] < mynum:
                zero=middle+1
            else: 
                lenghtOfArr = middle - 1
    return -1
  

arr = [ 2, 3, 4, 10, 40 ]
find_x = 10

result = b_search(arr, 0, len(arr)-1, find_x) 

if result==-1:
    print("Not found .")
else:
    print("Index Of : ",result)