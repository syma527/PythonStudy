"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/15 20:41
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一个类继承多个类【不推荐使用】了解
按继承顺序(从左往右)去对应的父类去找方法和属性
1、继承多个类，属性和方法谁有就执行谁的(方法和属性不重复的情况下)
2、如果继承多个类，多个父类有相同的方法和属性，按照从左往右的顺序去查找，找到了就执行或者使用

class A:
    def __init__(self):
        print("A")
    def test_01(self):
        print("A>>test_01")

class B:
    def __init__(self):
        print("B")
    def test_01(self):
        print("B>>test_01")

class C(B,A,):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    cl = C()
    cl.test_01()
    #打印类的继承顺序
    print(C.__mro__)
    

"""
#错误案例，不要这么写
class A:
    def __init__(self):
        print("A")
    def test_01(self):
        print("A>>test_01")

class B(A):
    def __init__(self):
        print("B")
    def test_01(self):
        print("B>>test_01")

class C(A,B):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    cl = C()
    cl.test_01()
    #打印类的继承顺序
    print(C.__mro__)