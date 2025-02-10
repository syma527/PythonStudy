"""
class Demo:
    # 私有类属性
    __name = "张三"
    color = "red"

    def __init__(self):
        # 私有类属性
        self.__age = 20
        self.size = 100

    def test_01(self):
        #私有属性只能在类内部使用
        print(self.__age)
        print(self.__name)

cl = Demo()
print(cl.size)
print(cl.age)
"""
class Demo:
    def __init__(self):
        self.age = 20
        self.name = "张三"

    def test_01(self):
        print("hello")

cl = Demo()
cl.name = "李四"
print(cl.name)
cl.test_01()


