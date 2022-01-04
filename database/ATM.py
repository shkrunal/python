import sqlite3
from sqlite3.dbapi2 import Cursor
penny=[]
GG=[]
def connection():
    a = sqlite3.connect('ATM04.db')
    return a

def createTab(a):
    a.execute('''CREATE TABLE IF NOT EXISTS ATM04(ACCOUNT INTEGER  PRIMARY KEY, NAME TEXT,PASSWORD INT,AMOUNT INT)''')

def Insert(a):
    n = int(input("Enter How Many People :"))
    for i in range(n):
        AA0 = int(input("Enter Account Number :"))
        AA1 = input("Enter Your Name :")
        AA2  = int(input("Create Your 4 Digit Password Here :"))
        AA3 = int(input("Enter Amount :"))
        print("Account Created")
        a.execute("INSERT INTO ATM04(ACCOUNT,NAME,PASSWORD,AMOUNT) VALUES(?,?,?,?)",(AA0,AA1,AA2,AA3))

def retrieve(a):
    cursor = a.cursor()
    id = int(input("REEnter Your ACCUNT NO :"))
    User = int(input("REEnter Your PIN :"))
    penny.append(id)
    B1 = "SELECT * FROM ATM04 WHERE ACCOUNT =?"
    A1 = "SELECT * FROM ATM04 WHERE PASSWORD=?"
    if A1 and B1 :
        cursor.execute(A1,(User,))
        cursor.execute(B1,(id,))
        rows =  cursor.fetchall() 
    for row in rows:
        continue  
    if row[0]==id and row[2]==User:
        print("**\tWelcome To Online ATM :)")
        class atm():
            def amount(self,a):
                self.a=a
                return self.a
            def deposit(self,b):
                self.b=b
                self.a=self.a+self.b
                return self.a
            def withdraw(self,c):
                self.c=c
                if self.a>=c:
                    self.a=self.a-self.c
                else:
                    print("insuficient balance :")
                return self.a
            def finalamount(self):
                return self.a

        x=atm()
        n=row[3]
        print(x.amount(n))
        while True:
            print("\n1 --> deposit")
            print("2 --> withdraw")
            print("3 --> exit")
            z=int(input("Please enter 1 or 2 or 3 :"))
            if z==1:
                nn=int(input("Enter Amount To Deposit :"))
                print(x.deposit(nn))
            elif z==2:
                nnn=int(input("Enter Amount To Withdraw :"))
                print("Remaining Balance :",x.withdraw(nnn))
            elif z==3:
                print("Final Balance in your Account :",x.finalamount())
                GG.append(x.finalamount())
                break
            else:
                break

    else:
        print("\tData Match Not Found :(")
        print("<<< Try Again >>>")
        retrieve(a)

def update(a):
    cursor=a.cursor()
    hq=penny[0]
    fc=GG[0]
    zef="UPDATE ATM04 SET AMOUNT=? WHERE ACCOUNT=?"
    cursor.execute(zef,(fc,hq))
    
X = connection()
createTab(X)
A1 = Insert(X)
retrieve(X)
update(X)
X.commit()
X.close()



