class Father:
    def __init__(self):
        self.hair = "地中海"
        # 私有属性不能被继承
        self.__heigh = 170

    def car(self):
        print("爸爸的车")

    def __money(self):
        print("爸爸的私房钱")


class Son(Father):
    def car(self):
        super.car()
        print("自己买的奔驰")


if __name__ == '__main__':
    cl = Son()
    cl.car()
    super(Son,cl).car()