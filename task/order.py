a=['y','y','y','n','y','y','n','m','m']
count=0
n=[]
y=[]
m=[]
for i in a:
    count=count+1
    if i=='n':
        n.append(count)
        continue
    elif i=='y':
        y.append(count)
        continue
    else:
        m.append(count)
        continue
print("no is:",n)
print("yes is:",y)
print("move is:",m)
    
