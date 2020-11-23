ct = 1
mtx = []
val = int(input("Enter values to create a matrix :  "))

for i in range(val) :
  for x in range(1, val + 1) :
    if x != ct :
      mtx.append(0)
    else :
      mtx.append(1)
  ct += 1
  print(mtx)