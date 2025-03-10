"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/11 20:49
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
记住这三句话：
类访问类属性，类实例访问所有属性
双下划线开头的属性就叫私有属性
作用域改变了，只能在类的内部访问，不能在类外面访问

私有属性
1、定义：双下划线开头的属性就叫私有属性
2、特性
   1、作用域改变了，只能在类的内部访问，不能在类外面访问
3、强行访问
print(Demo.clolr)
print(Demo._Demo__name)
print("实例的所有属性：",cl.__dict__)
print(cl._Demo__age)

"""
class Demo:
    #私有类属性
    __name = "张三"

    clolr = "red"

    def __init__(self,age):
        #私有实例属性
        self.__age = age
        self.size = "100"

    def test_01(self):
        #私有属性只能在类内部使用
        print(self.__age)
        print(self.__name)

cl = Demo(20)

#私有属性不能在类外部访问
# print(Demo.__name)
# print(cl.__age)

# cl.test_01()

#打印对象的所有属性
import pprint
print("类的所有属性")
pprint.pprint(Demo.__dict__)

#强行访问私有属性，拓展
print(Demo.clolr)
print(Demo._Demo__name)
print("实例的所有属性：",cl.__dict__)
print(cl._Demo__age)


