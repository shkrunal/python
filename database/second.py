import sqlite3

def connection():
    a=sqlite3.connect("sum.db")
    return a

def create_t(a):
    a.execute(''' CREATE TABLE COMPENY(NAME TEXT,PRICE INT PRIMARYKEY) ''')
    print("done")

def insert(a):
    k=int(input("enter value :"))
    i=1
    while i<=k:
        n=input("Enter name :")
        p=int(input("enter prize:"))
        i=i+1
        a.execute("INSERT INTO COMPENY(NAME,PRICE)values(?,?)",(n,p))
    b=a.execute("SELECT PRICE FROM COMPENY ")
    for i in b:
        print(i)
    print("inserted")

o=connection()
insert (o)
o.commit()
o.close()
