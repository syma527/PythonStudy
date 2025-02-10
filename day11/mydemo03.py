class Demo:
    def __init__(self,name):
        self.name = name

    def test_01(self):
        print("test_01实例方法")

    @classmethod
    def test_04(cls):
        print("test_04类方法")


    @classmethod
    def test_03(cls):
        print("test_03类方法")
        cls.test_04()

    def test_02(self):
        self.test_03()
        print("test_02实例方法")

cl = Demo("张飒")
print(cl.name)
cl.test_03()
cl.test_02()
Demo.test_03()