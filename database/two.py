import sqlite3
d={'name':None,'subject':None,'marks':None,'total':None,'percentage':None}

def connection():
    a=sqlite3.connect("stu2.db")
    return a

def create_t(a):
    a.execute(''' CREATE TABLE IF NOT EXISTS STU_FUN(NAME TEXT,SUB TEXT,MARKS TEXT,TOTAL INT,PERCENTAGE INT) ''')
    print("done")

def insert(a):
     a.execute("INSERT INTO STU_FUN(name,sub,marks,total,percentage)values(?,?,?,?,?)",(d['name'],d['subject'],d['marks'],d['total'],d['percentage']))
     a.commit()

def select(a):
    b=a.execute("SELECT * FROM STU_FUN")
    c=b.fetchall()
    print(c)

def student(o):
    n=int(input("how many students:"))
    name(n,o)

def name(x,o):
    for i in range(x):
        name=input("\nenter name: ")
        d['name']=name
        s=int(input("how manny subjects:"))
        subject(s)
        insert(o) 

def subject(s):
    total=0
    ss=''
    a=''
    for i in range(s):
        subname=input('Enter Subject Name : ')
        ss=ss+subname+","
        score=int(input('Enter Marks : '))
        m=score
        a=a+str(m)+','
        total=total+m
    
        d['subject']=ss
        d['marks']=a
        d['total']=total  
        totl(i,total)        
    print("inserted")

def totl(i,t):
    percentage(i+2,t)

def percentage(s,t):
    p=t/s
    d['percentage']=str(p)+'%' 

o=connection()
create_t(o)
student(o)
select(o)
o.close()