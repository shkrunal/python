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
        break
    else:
        print("Final Balance in your Account :",x.finalamount())
        break