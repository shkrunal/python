odd=[]
even=[]
s=[]
a=[0,1,2,3,4,5,6,7,8,9,11,14]
for i in a:
    if i==0 or i==1:
        s.append(i)
    elif i%2==0:
        odd.append(i)
    else:
        even.append(i)
    
print("odd number is:",odd)
print("even number is:",even)
print("special number is:",s)
