"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/15 20:32
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
三、多继承【了解】
多重继承
1、自己有的方法和属性优先用自己的，自己没有就用爸爸的，爸爸没有就用爷爷的，一次往上寻找




"""
class A:
    def __init__(self):
        print("A")

    def test_01(self):
        print("A>>test_01")

class B(A):
    def __init__(self):
        super().__init__()
        print("B")
    def test_02(self):
        print("B>>test_01")

class C(B):
    def __init__(self):
        super().__init__()
        print("C")
    def test_01(self):
        print("C>>test_01")


if __name__ == '__main__':
    cl = C()
    cl.test_01()
    #打印类的继承顺序
    print(C.__mro__)


