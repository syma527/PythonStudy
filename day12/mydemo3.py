class Father:
    def __init__(self):
        self.hair = "地中海"
        #私有属性不能被继承
        self.__heigh = 150

    def car(self):
        print("爸爸的车")

    def money(self):
        print("dad's money")

    def __money(self):
        print("dad's secret purse")

class Son(Father):
    def car(self):
        super(Son, self).car()
        print("自己买的奔驰")

if __name__ == '__main__':
    cl = Son()
    cl.car()