"""
class Father:
    def __init__(self,name):
        self.name = name
        print("父类的初始化方法")

    def test_01(self):
        print("父类的test01打印",self.name)

class Son(Father):
    def __init__(self,name):
        print("子类的初始化方法")

        super().__init__(name)
if __name__ == '__main__':
    cl = Son("zhangsan")
    cl.test_01()



class Base(object):
    def __init__(self):
        print("enter Base")
        print("leave Base")

class A(Base):
    def __init__(self):
        print("enter A")
        super(A,self).__init__()
        print("leave A")

class B(Base):
    def __init__(self):
        print("enter B")
        super(B,self).__init__()
        print("leave B")

class C(A,B):
    def __init__(self):
        print("enter C")
        super(C,self).__init__()
        print("leave C")

c = C()
print(C.mro())

"""


class A:
    def __init__(self):
        print("A")

    def test_01(self):
        print("A>>test_01")


class B(A):
    def __init__(self):
        super(B, self).__init__()
        print("B")

    # def test_01(self):
    #     print("B>>test_01")


class C(B):
    def __init__(self):
        super().__init__()
        print("C")

    # def test_01(self):
    #     print("C>>test_01")

if __name__ == '__main__':
    cl = C()
    cl.test_01()