class student_info:
    
    def stu(self):
        name=input("enter name :")
        self.name=name
        sub=int(input("enter subject :"))
        self.sub=sub
        marks=[]
        self.marks=marks
        for i in range(sub):
            mark=int(input("enter marks :"))
            marks.append(mark)
            self.marks=marks
        return marks

    def data(self):
        a=self.name
        b=self.sub
        c=self.marks
        return a,b,c

        
class teacher(student_info):
    def t(self):
        name=input("enter name:")
        self.name=name
        div=input("enter division:")
        self.div=div

    def data(self):
        a=self.name
        b=self.div
        super().data()
        return a,b


class hod(teacher):
    def h(self):
        s=int(input("how manny teacher:"))
        na=[]
        self.na=na
        sa=[]
        self.sa=sa
        for i in range(s):
            n=input("enter name:")
            na.append(n)
            self.n=n
            salary=int(input("enter teacher salary:"))
            sa.append(salary)
            self.salary=salary
        return na , sa
    def data(self):
        a=self.na
        b=self.sa
        super().data()
        return a,b
        
while True:
    print("MULTILEVEL INHERIHERITANCE")
    main=int(input("ENTER 1 FOR HOD 2 FOR TEACHER 3 FOR STUDENT 4 FOR EXIT :"))
    if main==1:
        a=hod()
        print()
        q=int(input("ENTER 1 FOR TEACHER SALARY 2 FOR TEACHER DATA :"))
        if q==1:
            print(" TEACHER SALARY :",a.h())
        elif q==2:
            print(" TEACHER DATA :",a.data())

    elif main==2:
        b=teacher()
        print()
        w=int(input("ENTER 1 FOR STUDENT DIV 2 FOR STUDENT DATA :"))
        if w==1:
            print("STUDENT NAME AND DIVISION :",b.t())
        elif w==2:
            print("STUDENT DATA :",b.data())

    elif main==3:
        c=student_info()
        print()
        e=int(input("ENTER 1 FOR STUDENT INFO 2 FOR STUDENT MARKS :"))
        if e==1:
            print("STUDENT INFO :",c.stu())
        elif e==2:
            print("STUDENT MARKS :",c.data())

    elif main==4:
        break