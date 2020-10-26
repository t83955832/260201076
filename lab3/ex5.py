

day=int(input("enter input day"))
month=input("enter input month")

if 1<=day<=20 and month=="March" or month=="April" or month=="May":
    print("Spring")
elif 1<=day<=21 and month=="June" or month=="July" or month=="August":
    print("Summer")
elif 1<=day<=22 and month=="September" or month=="October" or month=="November":
    print("Fall")
elif 1<=day<=21 and month=="December" or month=="January" or month=="February":
    print("Winter")
else:
    print("more pay attention")