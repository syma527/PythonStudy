class Father:
    def __init__(self,name):
        self.name = name
        print("父类初始化方法")

    def test_01(self):
        print("父类test_01打印",self.name)

class Son(Father):

    def __init__(self, name):
        print("子类初始化方法")
        super().__init__(name)

    def test_01(self):
        print("子类test_01打印", self.name)

if __name__ == '__main__':
    cl  = Son(name)