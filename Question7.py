print("Donner le cout ")
x=int(input())
if x<0 : 
    print("Bro what are you doing")
else :
    if x<200 :
        p=x-x*0.001 
    if (x>=200) and (x<500) :
        p=x-x*0.003   
    if x>=500 :
        p=x/2
print(p)        