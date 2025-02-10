"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/13 21:31
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""

"""
一、私有方法：
1、定义的时候以双下划线开头的方法，叫私有方法
2、使用：作为对外调用方法的辅助方法，不希望被外部调用的时候就定义为私有方法
3、私有方法作用域：只能在类的内部被使用(不要去强制访问)
4、实例方法、类方方法、静态方法都可以定义为私有方法
5、一个下划线定义的方法和属性实际上可以直接使用，但是不建议使用

类的特性
一、封装
1、代码内部实现不让调用者知道，不暴露出来，只提供某些功能




"""
class Demo:

    def __handle_num(self,x,y):
        if not  isinstance(x,int):
            x = int(x)
        if not isinstance(y,int):
            y = int(y)
        return x,y

    def add(self,x,y):
        x , y = self.__handle_num(x,y)
        return x+y

    @classmethod
    def __test_01(cls):
        print("test_01")

    @staticmethod #私有静态方法
    def __test_02():
        print("test_02")

    #一个下划线定义的方法和属性实际上可以直接使用，但是不建议使用
    def _test_03(self):
        print("test03")

if __name__ == '__main__':
    cl = Demo()
    cl._test_03()

    # print(cl.add("1", 6))





