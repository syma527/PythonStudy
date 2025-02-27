class Father:
    def __init__(self, name = "zhangsan"):
        self.name = name
        print("父类初始化方法")

    def test_01(self):
        print("父类test_01打印", self.name)

class Son(Father):
    def __init__(self, name= "zhangsan ", age=20):
        super().__init__(name)
        self.age = age



    def test_01(self):
        print("子类test_01 打印", self.name,"年龄",self.age)

if __name__ == '__main__':
    cl = Son()
    cl.test_01()