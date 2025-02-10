class Father:
    def __init__(self):
        self.hair = "地中海"

    def money(self):
        print("爸爸的钱")

    def car(self):
        print("爸爸的车")

    # 私有方法不能被继承
    def __money(self):
        print("爸爸的私房钱")

class Son(Father):
    def car(self):
        super().car()
        print("自己买的奔驰")

if __name__ == '__main__':
    cl = Son()
    print(cl.hair)
    cl.car()
    super(Son, cl).car()