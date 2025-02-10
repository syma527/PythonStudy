"""
class Demo:
    def __init__(self, name, age=20):
        self.name = name

    def test_01(self, name, age):
        print("hello")


if __name__ == '__main__':
    cl = Demo("zhangsan")
    cl.test_01("lisi", 20)
"""

class Demo:
    def __init__(self,age = 20):

        self.name = "张三"
        self.age = age
        print(self.age)
        print(self.name)

    def test_01(self):
        print(self.name)

if __name__ == '__main__':
    cl = Demo()

