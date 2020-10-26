
#If I leave my house at 6:52 am and run 1 mile
#at an easy pace (8 minutes per mile), then 3
#miles at tempo (6 minutes per mile) and 2 #mile
#at easy pace again, what time do I get home
#for breakfast?
hour,minutes,runPerMil,tempoPerMil=6,52,8*(1+2),6*3
newMinutes,newHours=(minutes+runPerMil+tempoPerMil)%60,(hour)+(minutes+runPerMil+tempoPerMil)//60
print(newHours,":",newMinutes)



