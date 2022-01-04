n=[1,2,3,4,5,6,7,8,9,10,11]
p=[]
np=[]
for i in n:
    if i==2 or i==3 or i==5 or i==7:
        p.append(i)
    elif i%2==0 or i%3==0 or i%5==0 or i%7==0:
        np.append(i)
    else:
        p.append(i)
print("prime",p)
print("not prime",np)