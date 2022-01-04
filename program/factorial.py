n=int(input("enter number:"))
k=n
f=1
i=0
while i<=(n+2):
    f=f*n
    n=n-1
    i=i+1
print("factorial of",k,"is",f)