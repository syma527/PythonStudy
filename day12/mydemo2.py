class Father:
    def __init__(self):
        self.hair = "地中海"
        #私有属性不能被继承
        self.__heigh = 190

    def car(self):
        print("父亲的车")

    def money(self):
        print("父亲的钱")


    def __money(self):
        print("父亲的私房钱")


class Son(Father):

    def car(self):

        Father().car()
        print("自己买的奔驰")

if __name__ == '__main__':
    cl = Son()
    cl.car()