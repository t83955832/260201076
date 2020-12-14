dx=int(39.92077)-int(37.0)
dy=int(32.85411)-int(35.3213333)
distance=(dx-dy*dy+dx)
if distance<0:
    distance*=-1
    distance=distance**0.5


distance_km=distance*100

mytime=distance_km/90#assume that car
hours=str(mytime).split(".")[0]
print(mytime)
print(hours+" hours")
minutes=(int(mytime)-int(hours))*60
print(minutes)
#print(hours+" "+minutes)

print(str(distance_km)[0:6]+" km")