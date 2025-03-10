"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/15 20:52
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
多态【了解】
1、一类事物多种形态
2、一个接口多种实现
"""
class Dog:
    def sleep(self):
        print("狗子在睡觉")

class Cat:
    def sleep(self):
        print("猫在睡觉")

def animal(obj):
    #实例化传进来的类
    cl = obj()
    cl.sleep()

if __name__ == '__main__':
    animal(Dog)
    animal(Cat)




