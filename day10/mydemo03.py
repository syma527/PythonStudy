class Car:
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def test_01(self):
        print(self.name,"车子开走了")

    def test_02(self):
        print(self.name,"车子刹车了")

car = Car(name="benz",color="grey")

car.test_01()