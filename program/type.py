a=[1,2,3,4,'j','k','l',5,6,'m']
inte=[]
ster=[]
for i in a:
    if type(i)==int:
        inte.append(i)
    else:
        ster.append(i)
print("integer value is:",inte)
print("string value is:",ster)