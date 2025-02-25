class Demo:
    def __init(self,name):
        self.name = name

    def test_01(self):
        print("test_01实例方法")

    @classmethod
    def test_02(cls):
        print("test_02类方法")

    @classmethod
    def test_04(cls):
        print("test_04类方法")

    def test_05(self):
        self.test_04()
        print("test_05实例方法")

