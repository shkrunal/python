class student():
    
    def marks(self):
        list=[]
        self.z=list
        m=int(input("enter num of subject :"))
        for i in range (m):
        #while m>=0:
            x=int(input(" enter marks:"))
            list.append (x)
        return self.z
    def per(self):
        l=len(self.z)
        s=sum(self.z)
        return s/l
    def attendence(self):
        return 2

class working_stu(student):
    def salary(self):
        return 'salary'

h=input("enter student or working_student :")
if h=='student':
    print(student())
elif h=='working_student':
    print(working_stu())


obj=student()
print(obj.marks())
print(obj.per())
print(obj.attendence())
# obj1=working_stu(student)
# print(obj1.salary())
# print(obj1.marks([10,20,30,40]))
# print(obj1.per())
