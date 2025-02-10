"""
class Demo:
    def __init__(self):
        print("构造方法")

    def test01(self, name):
        self.name = name
        print("实例方法")
        print(self.name)

fir = Demo()
fir.test01("zhangsan")
"""
"""
class Demo1:
    def test01(self):
        print("这是一个实例方法1")

    def test02(self):
        print("这是一个实例方法2")
        self.test01()
fir = Demo1()
fir.test02()

class Demo2:
    def __init__(self,age):
        self.age = age
        print("调用构造方法")

    def test01(self):
        print("实例方法1")

    def test02(self):
        print("实例方法2")
        self.test01()

    @classmethod
    def test03(cls):
        print("调用一下类方法")

    @staticmethod
    def test04():
        print("这是一个静态方法")

cl = Demo2("zhangsan")
cl.test02()
cl.test03()
cl.test04()
Demo2.test03()
Demo


class Demo2:
    @classmethod
    def test01(cls):
        print("调用类方法1")

    @classmethod
    def test02(cls):
        print("调用类方法2")
        cls.test01() # 未在方法内部，在外部就是属性。
Demo2.test02()

"""


class Demo1:
    def sum01(self, x, y):
        if not isinstance(x):
            x = int(x)
        if not isinstance(y):
            y = int(y)
        return x, y

    def sum02(self,x,y):
        print("please input %d and %d" %(x,y))
        return x + y

cl = Demo1()
x = cl.sum02(3,6)
print(x)