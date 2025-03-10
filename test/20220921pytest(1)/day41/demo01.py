"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/9/21 19:57
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
官网：https://docs.pytest.org/en/stable/
1、pytest它是通过钩子函数实现的，需要改造很困难

测试框架
1、unittest：python自带的单元测试框架
2、pytest：第三方开源测试框架
   pip install pytest==6.2.2
   
unittest与pytest的区别
1、unittest简单容易上手，对初学者很友好
2、pytest：功能上更强大，使用更灵活，封装更强
3、pytest支持重运行，unittest不支持错误重运
4、pytest和allure测试报告一起使用【支持插件】
5、unittest用例执行顺序按ASCII码顺序(文件+用例)
6、pytest测试用例文件：按ASCII码顺序；测试用例：py文件里面从上到下执行

unittest与pytest的共同点
1、测试流程一样的：写测试用例 -- 收集测试用例 -- 前后置处理 -- 执行测试用例 -- 生成测报告
2、测试用例的命名规范都一样
3、支持参数化
4、支持前后置
5、业务流程一样的
6、支持运行指定的测试用例
7、测试文件如果不是test_开头就不会被默认为测试用例文件


用例编写规范
unittest:
1、必须继承unittest.TestCase类
2、测试用例必须写在测试类里面
3、测试类：必须是Test开头
4、测试类里面不能写init方法
5、断言是unittest.TestCase自己封装的
6、用例收集(不支持打标签)
7、前后置：类级别、函数级别

pytest：
1、不需要继承，直接写就可以了
2、不一定要写在类里面，也可以直接写函数
3、测试类：可以不用Test开头(建议以Test开头,方便与unittest切换使用)
4、测试用例：以test_开头，或者_test结尾(建议以test_开头)
5、测试类里面不能写init方法
6、断言只能自己断言assert 表达式
7、用例收集方式很多种(类、用例文件、标签)
8、前后置: 支持自定义前后置，类级别、函数级别、会话级别、全局conftest.py


pytest框架的设置
setting -- tools --- python integrated tools -- testing -- default test runner -- 下拉选择pytest


运行测试用例
-s: 显示程序执行过程中的日志和print信息
-v: 显示执行的详细过程
pytest.main(['-s','-v'])


pytest的工作空间目录是rootdir,python文件运行的目录就是rootdir
rootdir: D:\vip_class\py52\day41


pytest如何收集测试用例的
1、确定你的rootdir目录
2、确认你的测试用例文件
3、确认测试用例文件的测试用例

"""
import pytest

def test_01():
    print("test01")

def test_02():
    print("test02")

class TestDemo:
    def test_03(self):
        print("test03")


if __name__ == '__main__':
    pytest.main(['-s','-v'])

