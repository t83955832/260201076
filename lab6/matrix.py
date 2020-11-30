ct = 1
mtx = []
lenMtx = int(input("Enter values to create a matrix :  "))

for i in range(lenMtx) :
  for x in range(1, lenMtx + 1) :
    if x != ct :
        mtx.append(0)
    else :
        mtx.append(1)
  ct += 1
  print(mtx)