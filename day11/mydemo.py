class Demo:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("这是实例属性方法",self.name)
        print("这是实例属性调用方法2",self.age)

    def  test01(self):
        print(self.age)
        print(self.name)

cl = Demo("xiaobu",30)
print("调用实例方法",cl)
print()

