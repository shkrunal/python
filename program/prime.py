n=int(input("enter number:"))
if n==2 or n==3 or n==5 or n==7:
    print(n,"number is prime")
elif n%2==0 or n%3==0 or n%5==0 or n%7==0:
    print(n,"number is not prime")
else:
    print(n,"number is prime")


