"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/13 21:46
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
二、继承
1、子类继承父类，子类就拥有了父类的方法和属性(私有方法和属性除外)
2、方法调用
   实例调用的情况：
   1、子类没有重写父类方法：调用父类的方法,方法查找顺序：子类---父类
   2、子类有重写父类的方法：调用自己的方法，方法查找顺序：子类---父类
   super()调用的情况：
   1、子类没有重写父类方法：调用父类的方法,方法查找顺序：父类
   2、子类有重写父类的方法：调用自己的方法，方法查找顺序：父类
3、重写父类方法
   子类有一个与父类方法名一样的方法，这个就叫重写父类的方法

三、多态


"""

class Father:
    def __init__(self):
        self.hair = "地中海"
        #私有属性不能被继承
        self.__heigh = 190

    def car(self):
        print("爸爸的车")

    def money(self):
        print("爸爸的钱")

    #私有方法不能被子类继承
    def __money(self):
        print("爸爸的私房钱")

class Son(Father):
    def car(self):
        # super(Son, self).car()
        super().car()
        print("自己买的奔驰")

if __name__ == '__main__':
    cl = Son()
    # print(cl.hair)
    # cl.money()
    # cl.car()
    super(Son, cl).car()

