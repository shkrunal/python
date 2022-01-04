class one():
    
    def __init__(self,b):
        self.b=b

    def balance(self):
        
        return self.b

    def deposite(self):
        b=int(input("enter deposite amount :"))
        self.b+=b
        return self.b

    def withdraw(self):
        c=int(input("enter withdraw amount :"))
        self.b-=c
        return self.b

for i in range(0,3):
    a=1234
    b=int(input("enter your pin :"))
    if b==a:
        print("your pin is correct")

        while True:
            print("\t:WELCOME TO ATM:")
            print("\t1:- FOR CHECK YOUR BALANCE :")
            print("\t2:- FOR WITHDREW MONEY :")
            print("\t3:- FOR DEPOSITE MONEY :")
            print("\t4:- FOR EXIT :")



            ch=int(input("ENTER YOUR CHOICE : "))


            obj=one(1000)

            if ch==1:
                print("YOUR BALANCE IS :",obj.balance())
            elif ch==2:
                print("YOUR WITHDRAW :",obj.withdraw())
            elif ch==3:
                print("YOUR DEPOSITE :",obj.deposite()) 
            else:
                break
        break
    else:
        print("your pin is wrong")