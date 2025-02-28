from idlelib.run import manage_socket


class Father:
    def __init__(self, name):
        self.name = name
        print("父类初始化方法")

    def test_01(self):
        print("父类的test_01 打印",self.name)

class Son(Father):
    def __init__(self, name, age):

        self.age = age
        super().__init__(name)



if __name__ == '__main__':
    cl = Son(name="zhangsan", age = 30)
    cl.test_01()
