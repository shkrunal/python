a=int(input("Enter number :"))
i=1
while i<=a:
    n=input("Enter name :")
    s=int(input("Enter number subject :"))
    i=i+1
    j=1
    add=0
    p=0
    while j<=s:
        marks=int(input("enter marks:"))
        j=j+1
        add=add+marks
        p=(add/(s*100))*100

    print("total is :",add)
    print("persentage is:",p,"%")