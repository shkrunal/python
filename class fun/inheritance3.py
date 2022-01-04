class A:
    def __init__(self,name):
        print(f"{name} is good boy")
    def f2(self):
        print("f1")
class B(A):
    # def __init__(self,name1):
    #     print(f"{name1} is not good boy")    
    def f2(self):
        super().f2()

        print("f2")
class C(B):
    def __init__(self,name2):
        print(f"{name2} is bad boy")
    def f3(self):
        print("f3")


b=B("RAHUl")
b.f2()




