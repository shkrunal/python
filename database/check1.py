import sqlite3
class one():

    def connection(self):
            a=sqlite3.connect('ATM01.db')
            return(a)

    def create(self,a):
        a.execute('''CREATE TABLE IF NOT EXISTS ATM01(ACCNOUNT INT PRIMARYKEY,NAME TEXT,PIN INT,BALANCE INT)''')

    def insert(self,a):
        n = int(input("Enter How Many People :"))
        for i in range(n):
            A0 = int(input("Enter Account Number :"))
            A1 = input("Enter Your Name :")
            A2  = int(input("Create Your 4 Digit Password Here :"))
            A3 = int(input("Enter Amount :"))
            print("Account Created")
            a.execute("INSERT INTO ATM01(ACCOUNT,NAME,PIN,BALANCE) VALUES(?,?,?,?)",(A0,A1,A2,A3))
    
    def deposite(self):
        a=int(input("Enter amount you want to deposite:"))
        self.b+=a
        return self.b
    def withdraw(self):
        c=int(input("Enter amount you want to withdraw:"))
        self.b-=c
        return self.b
for i in range(0,3):
    a=1234
    b=int(input("Enter your pin:"))
    if b==a:
        print("Correct pin:")
        while True:
            print("\t\t:: WELCOME ::")
            print("1:- For Deposite Money  :")
            print("2:- For Withdrew Money      :")
            print("3:- For Exit      :")

            ch=int(input("Enter Your Choice :- "))

            obj=one()

            if ch==1:
                print("Your Balance Is :",obj.balance())
            elif ch==2:
                print("You Deposite :",obj.deposite())
            elif ch==3:
                print("You Withdraw :",obj.withdraw())
            else:
                break

    else:
        print("Incorrect pin:")