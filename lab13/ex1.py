def s_sort(numbers):
    
    for x in range(len(numbers)-1): 
        minValueOfIndex = x

        for y in range(x + 1,len(numbers)):
            if numbers[y] < numbers[minValueOfIndex] :
                minValueOfIndex = y

        if minValueOfIndex != x:
            temp = numbers[x]
            numbers[x] = numbers[minValueOfIndex]
            numbers[minValueOfIndex] = temp

    return numbers


sort_list = [55,25,78,2,17,98,13,5]

print(s_sort(sort_list))