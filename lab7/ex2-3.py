books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dict = {}
for i in books :
  print(i)
  length_str = len(i)
  un_str = len(list(set(i)))
  print(length_str)
  print(un_str)
  average = (length_str+un_str)/2
  current_tup = (length_str , un_str , average)
  book_dict[i] = current_tup
print(book_dict)
    