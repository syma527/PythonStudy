class Demo:
    def __init__(self,name):
        self.name = name

    def test_03(self):
        print("test_03实例方法")

    @classmethod
    def test_04(cls):
        print("test_04类方法")

    @classmethod
    def test_01(cls):
        print("类方法")

    def test_02(self):
        self.test_01()
        print("test_02实例方法")

cl = Demo("张三")
cl.test_01()
Demo.test_01()