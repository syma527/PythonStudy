class Person:
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def test_01(self):
        print(self.name,"车子开走了")

    def test_02(self):
        print(self.color,"车子刹车了")

    def test_03(self):
        print(self.name,"车子按喇叭")

person1 = Person('zhangsan','green')

person1.test_01()
person1.test_03()
person1.test_02()