class Demo:
    __name = "张三"
    color = "red"

    def __init__(self):
        self.age = 20
        self.size = 100

    def test_01(self):
        print(self.__age)
        print(self.__name)

cl = Demo()
print(cl.size)
print(cl.age)

import pprint

pprint.pprint(Demo.__dict__.values(color))