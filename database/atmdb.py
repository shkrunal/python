
import sqlite3
from sqlite3.dbapi2 import Cursor
penny=[]
GG=[]
class one():
    
    def connection(self):
        a=sqlite3.connect('ATM01.db')
        return(a)

    def create(self,a):
        a.execute('''CREATE TABLE IF NOT EXISTS ATM01(ACCNOUNT INT PRIMARYKEY,NAME TEXT,PIN INT,BALANCE INT)''')

    def insert(self,a):
        n = int(input("Enter How Many People :"))
        for i in range(n):
            AA0 = int(input("Enter Account Number :"))
            AA1 = input("Enter Your Name :")
            AA2  = int(input("Create Your 4 Digit Password Here :"))
            AA3 = int(input("Enter Amount :"))
            print("Account Created")
            a.execute("INSERT INTO ATM01(ACCOUNT,NAME,PIN,BALANCE) VALUES(?,?,?,?)",(AA0,AA1,AA2,AA3))

    def retrieve(self,a):
        cursor = a.cursor()
        id = int(input("REEnter Your ACCUNT NO :"))
        User = int(input("REEnter Your PIN :"))
        penny.append(id)
        B1 = "SELECT * FROM ATM01 WHERE ACCOUNT =?"
        A1 = "SELECT * FROM ATM01 WHERE PIN=?"
        if A1 and B1 :
            cursor.execute(A1,(User,))
            cursor.execute(B1,(id,))
            rows =  cursor.fetchall() 
        for row in rows:
            continue  
        if row[0]==id and row[2]==User:
            print("\t:WELCOME TO ATM:")
            

    def balance(self):
        return self.b

    def acno(self):
        k=int(input("Enter Account Number : "))
        self.b=k
        return self.b

    def deposite(self):
        b=int(input("enter deposite amount :"))
        self.b+=b
        return self.b

    def withdraw(self):
        c=int(input("enter withdraw amount :"))
        self.b-=c
        return self.b
                
    def finalamount(self):
        while True:
            print("\t:WELCOME TO ATM:")
            print("\t1:- FOR DEPOSITE MONEY :")
            print("\t2:- FOR WITHDREW MONEY :")
            print("\t3:- FOR EXIT :")
            

            ch=int(input("ENTER YOUR CHOICE : "))

            if ch==1:
                nn=int(input("Enter Amount To Deposit :"))
                
            elif ch==2:
                nnn=int(input("Enter Amount To Withdraw :"))
                
            elif ch==3:
                
                break
            else:
                break
        
    def update(self,a):
        cursor=a.cursor()
        hq=penny[0]
        fc=GG[0]
        zef="UPDATE ATM04 SET AMOUNT=? WHERE ACCOUNT=?"
        cursor.execute(zef,(fc,hq))

z=one()