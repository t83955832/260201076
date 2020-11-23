mail=input("Please, enter your maila address E.g (abc@def.com)")

referenceMail="ceng113@iyte.edu.tr"

if '@' in mail:
    mail=mail.lower()
    part1=mail.split('@')[0]
    part1=part1.replace('.','')
    part_2 = mail.split("@")[1]
    mail = part1 + "@" + part_2
    print(mail)
    
if mail == referenceMail:
    print("Equal")
else:
    print("Not equal")

print("Not equal")








