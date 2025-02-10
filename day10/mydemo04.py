"""
def test_01():
    print("test_01")
    print("test02")
    test_02()
    test_03()


def test_02():
    print("这是打印出来test_02")


def test_03():
    print(dict("user": "ssss", "pwd": "123456"))

test_01()
"""


class Car:

    # 初始化方法
    def __init__(self, name, color):

        self.name = name
        self.color = color
        print("__init__中打印self", self)

    # 行为1
    def test_01(self):
        print(self.name, '车子开走了')

    # 行为2
    def test_02(self):
        print(self.name, '车子停下来')

    def test_03(self):
        print(self.name, "车子停住了")


car1 = Car(name="宝马", color="red")
print("外面打印的实例", car1)
car1.test_01()
car1.test_03()
