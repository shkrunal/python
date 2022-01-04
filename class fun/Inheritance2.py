class student:
    def __init__(self):
        name=input("Enter name:")
        self.name=name
        school=input("Enter school name:")
        self.school=school
        sub=int(input("enter number of sub :"))
        mark=[]
        for i in range(sub):
            marks=int(input("Enter marks:"))
            mark.append(marks)
            self.marks=mark
    def average(self):
        return sum(self.marks)/len(self.marks)

class WorkingStudent(student):
    def __init__(self):
        super().__init__()
        salary=int(input("enter your salary:"))
        self.salary=salary
    
    def func2(self):
        #avg=super().average()
        total=sum(self.marks)
        print(total)

    def weeklysalary(self):
        self.salary=self.salary*7
        return self.salary
h=int(input("enter 1 for student or 2 for workingstudent :"))
if h==1:
    anna=student()
    print(anna.average())
    print(anna.school)
elif h==2:
    rolf=WorkingStudent()
    rolf.func2()
    print(rolf.average())
    print(rolf.weeklysalary(),rolf.salary,rolf.school)







