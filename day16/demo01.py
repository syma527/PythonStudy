"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/22 20:11
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""


"""
测试用例包含哪些东西
   1、前置条件
   2、测试步骤(业务逻辑)
   3、断言(响应、数据库数据断言)
   4、数据提取
   5、后置处理
   6、测试报告
   7、邮件发送
   8、日志收集


一、前置后置
1、前后置方法不需要手动调用，会自动执行
2、前后置方法可以不写，按自己需求来写
3、前后置方法跟书写顺序没有关系，只要在测试用例类的内部都会被执行
函数级别的前置
def setUp(self) -> None:
    print("函数级别前置，每个测试用例执行之前执行一次")

类级别的前置
@classmethod
def setUpClass(cls) -> None:
    print("类级别前置，每个测试类执行之前执行一次")

函数级别的后置
def tearDown(self) -> None:
    print("函数级别的后置，每个测试用例执行结束之后执行一次")

类级别的后置
@classmethod
def tearDownClass(cls) -> None:
    print("类级别后置，每个测试类执行之结束之后执行一次")

"""
import unittest
#最完整的测试用例，没有用数据驱动
class TestDemo1(unittest.TestCase):
    #函数级别的前置
    def setUp(self) -> None:
        print("函数级别前置，每个测试用例执行之前执行一次")

    #类级别的前置
    @classmethod
    def setUpClass(cls) -> None:
        print("类级别前置，每个测试类执行之前执行一次")

    #函数级别的后置
    def tearDown(self) -> None:
        print("函数级别的后置，每个测试用例执行结束之后执行一次")

    #类级别的后置
    @classmethod
    def tearDownClass(cls) -> None:
        print("类级别后置，每个测试类执行之结束之后执行一次")

    def test_01(self):
        print("test_01")

    def test_02(self):
        print("test_02")


if __name__ == '__main__':
    unittest.main()

    # cl = TestDemo()
    # cl.tearDown()
    # TestDemo.tearDownClass()



