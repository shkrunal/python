a=int(input("enter number:"))
na=[]
ka=[]
for i in range(a):
    name=str(input("enter name:"))
    na.append(name)
    s=int(input("how many subjects:"))
    add=0
    for j in range(s):
        n=int(input("Enter marks :"))
        add=add+n
    print("total is :",add)
    ka.append(add)
print(na)
print(ka)

