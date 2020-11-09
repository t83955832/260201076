enteryear=int(input('enter a year'))

if enteryear%4==0:
  if enteryear%400==0:
    print('leap year')
  elif enteryear%100==0:
    print('not leap year')
  else:
    print('leap year')
else:
  print('not leap year')