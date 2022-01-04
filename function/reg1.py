import re
def name():
    a=str(input("enter name :"))
    patt=r'^[a-z]{3,8}$'
    g=re.match(patt,a)
    if g:
        number()
    else:
        name()

def number():
    k=input("enter number :")
    b=str(k)
    patt='^[0-9]{10}$'
    c=re.match(patt,b)
    if c:
        mail()
    else:
        number()

def mail():
    q=(input("enter mail :"))
    patt=r'^[a-z]{3,12}[0-9]{0,4}@gmail|yahoo.com|in$'
    g=re.match(patt,q)
    if g:
        password()
    else:
        mail()

def password():
    s=(input("enter password :"))
    patt=''
    g=re.match(patt,s)
    if g:
        print("your data successfully added ")
    else:
        password()

name()
