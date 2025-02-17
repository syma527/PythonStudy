from unittest import TestCase

class Demo:
    def __init(self,name):
        self.name = name

    def test_02(self):
        print("test_02实例方法")

    @classmethod
    def test_04(cls):
        print("test_04类方法")

    @classmethod
    def test_01(cls):
        print("test_01类方法")
        cls.test_04()

    def test_05(self):
        self.test_01()
        print("test_05实例方法")

cl  = Demo("李四")
cl.test_01()


Demo.test_01()