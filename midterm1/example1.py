
file_name=input("Enter a file path:")
file=open(file_name,"r")
texts=file.readlines()
texts="".join(texts).split(" ")
letters=input("Enter a list of letters:")
mylet=""

for i in letters:
    if i.isalpha():
        mylet+=i

while letters!="quit":

    if letters=="":
        print("Invalid input.")
    

    for letter in mylet:
        longestWord=""
        for word in texts:
            if letter in word:
                if len(word)>len(longestWord):
                    longestWord=word
        if longestWord!="":
            print(letter.lower()+" : "+longestWord.replace(".","").replace(",","").replace("“","").replace("”","").replace("\n","").replace("The","").replace("'","").lower())
        else:print(letter.lower()+" : "+"Letter not found!")
    mylet=input("Enter a list of letters:")
letter,longestWord="",""
print("Goodbye!")
file.close()