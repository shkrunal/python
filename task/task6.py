n=int(input("enter number:"))
k=n
f=1
for i in range(n):
    f=f*n
    n=n-1
print("factorial of",k,"is",f)