"""
class Dog:
    def sleep(self):
        print("狗子在睡觉")

class Cat:
    def sleep(self):
        print("猫在睡觉")

def animal(obj):
    print("动物们在睡觉")
    cl = obj()
    cl.sleep()
if __name__ == '__main__':
    animal(Dog)
"""


# class Demo:
#     name = "zhangsan"
#     age = 30
#     def __init__(self, age, name):
#        pass
#
# if __name__ == '__main__':
#     cl = Demo()
#     print(cl.__dict__)

class Demo:
    def __init__(self):
        pass


if __name__ == '__main__':
    cl = Demo()
    print(cl.__dict__)
    setattr(cl, "python", "51")
    res = getattr(cl, "pytn","sss")
    print(res)
    res2 = hasattr(cl,"python")
    print(res2)