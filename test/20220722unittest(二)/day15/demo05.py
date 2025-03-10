"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/20 21:32
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、unittest
1、python自带的单元测试框架，不用安装

二、四大核心组件
1、TestCase: 测试用例类，用来写测试用例的
2、TestSuite: 测试套件，用来装测试用例的
3、TextTestRunner：执行引擎，用来运行测试用例的
4、TestFixture：测试前置后置，用来完成用例执行的前置条件和后置清理工作
test_list = []
test_list.append(1)
test_list.append(2)
test_list.append(3)
print(test_list)

5、工作流程
   1、先用TestCase写测试用例，
   2、通过TestFixture写前置处理，
   3、通过TestSuite收集测试用例
   4、通过TextTestRunner执行测试用例，生测试报告(不用这个报告)
   
6、测试用例书写步骤
   1、导入 unittest 模块
   2、创建测试用例类，一定要继承unittest.TestCase，测试类建议以Test开头
   3、写一个测试用例，def test_*()，必须是test_开头的方法(实例方法)
   4、运行测试用例，从main函数运行，unittest会自动收集测试用例
   
7、测试用例包含哪些东西
   1、前置条件
   2、测试步骤(业务逻辑)
   3、断言(响应、数据库数据断言)
   4、数据提取
   5、后置处理
   6、测试报告
   7、邮件发送
"""
import unittest
class TestDemo(unittest.TestCase):

    def test_01(self):
        print("这里是测试用例要做的事情")
        print("test_01")

    def test_02(self):
        print("test_02")

if __name__ == '__main__':
    #框架执行入口main函数，会自动收集用例
    unittest.main()



