a=int(input("how many stu:"))
n=[]
for i in range(a):
    name=input("enter name:")
    n.append(name)
    s=int(input("how manny subjects :"))
    add=0
    for i in range(s):
        marks=int(input("enter marks:"))
        add=add+marks
    print("total is :",add)
    
print(n)
