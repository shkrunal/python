def salary(a,b):
    i=1
    k=[]
    v=[]
    while i<=a:
        n=input("name:")
        v.append(n)
        s=int(input("salary:"))
        i=i+1
        t=s*b/100
        print("add:",t)
        total=s+t
        k.append(total)
    return v , k
a=salary(2,10)
print(a)