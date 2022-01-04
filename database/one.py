import sqlite3

def connection():
    a=sqlite3.connect("new2.db")
    return a

def create_t(a):
    a.execute(''' CREATE TABLE STUDENT(NAME TEXT,AGE INT) ''')
    print("done")

def insert(a):
    z=input("enter name:")
    i=int(input("enter age:"))
    a.execute("INSERT INTO STUDENT(name,age)values(?,?)",(z,i))
    print("inserted")

o=connection()
create_t(o)
insert (o)
o.commit()
o.close()