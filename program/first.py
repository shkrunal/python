a=int(input("enter value A:"))
b=int(input("enter value B:"))
c=int(input("enter value 1 for add 2 for sub 3 for multi 4 for div:"))
if c==1:
    print("your answer is :",a+b)
elif c==2:
    print("your answer is :",a-b)
elif c==3:
    print("your answer is :",a*b)
elif c==4:
    print("your answer is :",a/b)
else:
    print("enter valid input")    