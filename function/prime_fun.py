def prime(i):
    if i==2 or i==3 or i==5 or i==7:
        n='prime'
    elif i%2==0 or i%3==0 or i%5==0 or i%7==0:
        n='not prime'
    else:
        n='prime'
    return n
a=prime(169)
print(a)