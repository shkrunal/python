class student:
    def __init__(self,name,m,x):
        list=[]
        self.z=list
        name=input("enter your name :")
        self.name=name
        m=int(input("enter num of subject :"))
        self.m=m
        for i in range (m):
        #while m>=0:
            x=int(input(" enter marks:"))
            list.append (x)
            self.x=x
        return self.z
        
    def average(self):
        return sum(self.x)/len(self.x)

class working_stu(student):
    def __init__(self,name,school,mark,salary):
        super().__init__(name,school,mark)
        self.salary=salary
    
    def func2(self):
        #avg=super().average()
        total=sum(self.x)
        print(total)

    def weeklysalary(self):
        return self.salary*7

h=input("enter student or working_student :")
if h=='student':
    print(student())
elif h=='working_student':
    print(working_stu())

rolf=working_stu()
rolf.func2()
print(rolf.average())
print(rolf.weeklysalary(),rolf.salary,rolf)

anna=student()
print(anna.average())


