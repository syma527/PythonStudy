"""
import  os
print(__file__)
my_path = os.path.dirname(__file__)
print(my_path)
res = os.path.abspath("mydemo02.py")
print(res)

import os
res = os.path.join("vip_pass","py44","index.html")
print(res.replace("\\","/"))


class Person(object):
    def __init__(self,newName,newAge):
        self.name = newName
        self.age = newAge

zhangsan = Person("张三",18)
zhangsan.addr = "北京"
print(zhangsan.name)
print(zhangsan.age)
print(zhangsan.addr)

lisi = Person("李四",29)
print(lisi.name)
print(lisi.age)



二继承
1、子类继承父类，子类就拥有了父类的方法和属性
2、普通方法调用
 实例调用的情况：
 1、子类没有重写父类的方法，直接调用父类的方法，方法查找顺序：子类-->父类-->父类的父类-->object-->父类的父类的父类-->object-->object
 2、子类有重写父类的方法，（优先使用自己的方法），调用自己的方法，方法查找顺序: 子类--父类
 3、重写父类方法
 子类有一个与父类方法名一样的方法，优先使用子类的方法
 4、调用初始化方法
 1、子类没有写初始化方法
   实例化子类的时候，会自动调用父类的方法
 2、子类重写了初始化的方法



class Father:
    def __init__(self,name):
        self.name = name
        print("父类初始化方法")

    def test_01(self):
        print("父类的test01打印",self.name)

class Son(Father):
    def __init__(self,name):
        print("子类初始化方法")
        # 调用父类的初始化方法
        super().__init__(name)

if __name__ == '__main__':
    cl = Son(name= "py52")
    cl.test_01()



class Dog:
    def sleep(self):
        print("狗子在睡觉")

class Cat:
    def sleep(self):
        print("猫在睡觉")

def animal(obj):
    cl = obj()
    cl.sleep()

if __name__ == '__main__':
    animal(Dog)
    animal(Cat)



python反射 == 动态设置属性【掌握】
1.设置属性
可以给类设置属性，也可以给类实例设置属性
setattr()
2、获取属性
getattr()
如果不设置默认值，当key不存的时候会报错
3、判断属性
hasattr()
属性存在返回true，否则返回false
4、删除属性
delattr()

class Demo:
    pass

if __name__ == '__main__':
    print(Demo.__dict__)
    setattr(Demo,"python","52期")
    result = getattr(Demo,"pyt","51期")
    print(result)
    res2 = hasattr(Demo,"pythosssn")
    setattr(Demo,"python","55期")
    print(res2)

    print(Demo.__dict__)
"""

class Father:
    def __init__(self,name):
        self.name = name
        print("父类的初始化方法")

    def test_01(self):
        print("父类的test01打印",self.name)

class Son(Father):
    def __init__(self):
        print("子类初始化方法")
        super().__init__("zhangsan")
if __name__ == '__main__':
    cl = Son()
    cl.test_01()
