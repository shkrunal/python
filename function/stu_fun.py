def stu():
    n=int(input("how many students:"))
    name(n)
def name(z):
    i=1
    aa=[]
    while i<=z:
        name=input("enter name:")
        aa.append(name)
        s=int(input("how manny subjects:"))
        sub(s)
        i=i+1
    return aa

def sub(s):
    j=1
    marks=[]
    while j<=s:
        m=int(input("enter marks:"))
        marks.append(m)
        j=j+1
    total(marks,s)   

def total(m,s):
    su=sum(m)
    per=(su/(s*100))*100
    print("total is :",su)
    print("persentage is:",per)

stu()
