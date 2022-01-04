import sqlite3

def connection():
    a=sqlite3.connect("com.db")
    return a

def create_t(a):
    a.execute(''' CREATE TABLE COMPENY(NAME TEXT,LASTNAME INT) ''')
    print("done")

def insert(a):
    b=int(input("enter value:"))
    i=1
    while i<=b:
        n=input("Name =")
        l=input("Last name =")
        i=i+1
        a.execute("INSERT INTO COMPENY(NAME,LASTNAME)values(?,?)",(n,l))
    print("inserted")

o=connection()
insert (o)
o.commit()
o.close()