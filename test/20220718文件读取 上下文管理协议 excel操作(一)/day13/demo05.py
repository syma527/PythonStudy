"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/15 21:17
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""

"""
类，类实例都可以设置属性、修改属性、判断属性、删除属性

python反射==动态设置属性【掌握】
1、设置属性
可以给类设置属性，也可以给类实例设置属性
setattr()
2、获取属性
getattr()
如果不设置默认值，当key不存的时候会报错
3、判断属性
hasattr()
属性存在返回True，否则返回False
4、删除属性
delattr()

"""
class Demo:
    """多行注释"""
    #
    # name = ""
    # age = ""
    #
    # def __init__(self,age,name):
    #     pass
    pass

if __name__ == '__main__':
    # cl = Demo()
    # print(cl.__dict__)
    # setattr(cl,"python","52期")
    # result = getattr(cl,"pyt","51期")
    # print(result)
    # print(cl.__dict__)
    # res2 = hasattr(cl,"python")
    # print(res2)
    # delattr(cl, "python")
    # print(cl.__dict__)


    print(Demo.__dict__)
    setattr(Demo,"python","52期")
    result = getattr(Demo,"pyt","51期")
    print(result)
    print(Demo.__dict__)
    res2 = hasattr(Demo,"python")
    setattr(Demo, "python", "55期")
    print(res2)
    # delattr(Demo, "python")

    print(Demo.__dict__)





def test_01(name,age):

    pass





