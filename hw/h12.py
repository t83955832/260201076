#eq1,eq2=input("Enter the first equation:\n"),input("Enter the second equation:\n")
#newEquation1=eq1.split("=")[0]+eq1.split("=")[1].replace("-","_").replace("+","-").replace("_","+")
#newEquation2=eq2.split("=")[0]+eq2.split("=")[1].replace("-","_").replace("+","-").replace("_","+")
newEquation1="+3x-5y+10-5x"
newEquation2='-2x+4y+13'
sliced_eq_1=["+2x","+5y","+8"]
sliced_eq_2=["-2x","-1y","+12"]
ch=""
a,b,c,d,e,f=0,0,0,0,0,0
b_string,e_string="",""
for x in sliced_eq_1:
    if 'x' in x:
      a+=(int(x[0:len(x)-1]))
    elif 'y' in x:
      b+=(int(x[0:len(x)-1]))
    else:
      c+=int(x)
if b<0:
  b_string=str(b)
else:
  b_string='+'+str(b)
for x in sliced_eq_2:
    if 'x' in x:
      d+=(int(x[0:len(x)-1]))
    elif 'y' in x:
      e+=(int(x[0:len(x)-1]))
    else:
      f+=int(x)
if e<0:
  e_string=str(e)
else:
  e_string='+'+str(e)
print("Equations in the simplified form :")
simple_eq_1=str(a)+'x'+b_string+'y'+'='+str(c)
print(simple_eq_1)
simple_eq_2=str(d)+'x'+e_string+'y'+'='+str(f)
print(simple_eq_2)
a_divide_d=-(a/d)
last_eq_c=c+(a_divide_d)*f
last_eq_b=b+(a_divide_d)*e
result_y=last_eq_c/last_eq_b
result_x=(c-(b*result_y))/a
print("Solution")
print("X = ",int(result_x))
print("Y = ",int(result_y))






