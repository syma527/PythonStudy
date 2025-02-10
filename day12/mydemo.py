"""
class Demo:
    color = "red"

    def __init__(self,name):
        self.name = name

    @classmethod
    def test_01(cls):
        print("这是一个类方法")

    @staticmethod
    def test_02():

        print("调用类方法成功")

    def test_03(self):
        print("这是一个实例方法")
        self.test_02()
        print("实例方法调用静态方法")

    @staticmethod
    def test_04():
        print(Demo.color)



demo1 = Demo("zhangsan")
# demo1.test_04()
demo1.test_03()


class Demo1:
    def test_01(self):
        print("这是一个实例方法")

    def test_02(self):
        print("这是一个实例方法2")
        self.test_01()

cl = Demo1()
cl.test_02()
"""


class Demo1:
    name = "类属性"

    def __init__(self, age):
        self.age = age

    def test_01(self):
        print("实例方法1")

    def test_02(self):
        print("实例方法2")
        # 实例调用
        print(self.age)
        print(self.name)
de = Demo1(30)
de.test_02()
de.name = "zhangsan"
print(de.name)
de.age = 20
print(de.age)