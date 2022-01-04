class student_info():
    def stu(self):
        na=[]
        name=input("enter name :")
        na.append(name)
        self.na=na
        su=[]
        sub=int(input("enter subject :"))
        su.append(sub)
        self.su=su
        marks=[]
        for i in range(sub):
            mark=int(input("enter marks :"))
            marks.append(mark)
        self.marks=marks

    def data(self):
        return self.na,self.su,self.marks
        

while True:
    c=student_info()
    print()
  
    
    print("STUDENT INFO :",c.stu())

    print("STUDENT MARKS :",c.data())