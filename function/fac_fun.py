def fac():
    n=int(input("enter number:"))
    f=1
    i=0
    while i<=(n+2):
        f=f*n
        n=n-1
        i=i+1
    return f
a = fac()
print(a)