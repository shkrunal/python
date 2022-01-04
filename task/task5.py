a=int(input("how manny employee:"))
b=int(input("how manny increment:"))
i=1
h=[]
j=[]
while i<=a:
    n=input("name:")
    h.append(n)
    s=int(input("salary:"))
    i=i+1
    t=s*b/100
    print("add:",t)
    total=s+t
    j.append(total)
    print("total:",total)
print(h)
print(j)