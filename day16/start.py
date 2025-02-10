"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/22 20:54
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
用例执行入口
测试用例收集
一、测试用例维度【了解】
1、添加单个测试用例
su.addTest(TestDemo4("test_01"))
2、添加多个测试用例
su.addTests([TestDemo4("test_01"),TestDemo4("test_02")])
3、代码
from day16.demo04 import TestDemo4
import unittest
#创建测试套件：用来收集测试用例
su = unittest.TestSuite()
#把测试用例放到条件里
# su.addTest(TestDemo4("test_01"))
su.addTests([TestDemo4("test_01"),TestDemo4("test_02")])
#创建一个执行器
runner = unittest.TextTestRunner()
#将测试套件放到执行器去执行
runner.run(su)

二、测试类维度【了解】
1、收集对应的测试类下面的所有测试用例
su.addTest(unittest.makeSuite(TestDemo4))
unittest.defaultTestLoader.loadTestsFromTestCase(TestDemo4)
2、代码
from day16.demo04 import TestDemo4
from day16.demo03 import TestDemo3
import unittest
#创建测试套件：用来收集测试用例
su = unittest.TestSuite()
#把测试用例放到条件里
su.addTest(unittest.makeSuite(TestDemo4))
su.addTest(unittest.makeSuite(TestDemo3))
#创建一个执行器
runner = unittest.TextTestRunner()
#将测试套件放到执行器去执行
runner.run(su)

三、模块维度【掌握】
1、收集指定目录下的某些py文件下的测试用例类中的测试用例
start_dir="."：测试用例文件(.py)所在的目录
pattern='demo*.py：测试用例文件的名称，*表示通配符，默认是test开头的py文件
su = unittest.defaultTestLoader.discover(start_dir=".", pattern='demo*.py')
2、代码
import unittest
#创建测试套件：用来收集测试用例
su = unittest.defaultTestLoader.discover(start_dir=".", pattern='demo*.py')
#不建议这样写
# su = unittest.TestLoader().discover(start_dir=".", pattern='demo*.py')
#创建一个执行器
runner = unittest.TextTestRunner()
#将测试套件放到执行器去执行
runner.run(su)


测试报告
一、BeautifulReport生成测试报告
1、安装BeautifulReport包
pip install BeautifulReport
2、代码
import unittest
from BeautifulReport import BeautifulReport
#创建测试套件：用来收集测试用例
su = unittest.defaultTestLoader.discover(start_dir=".", pattern='demo*.py')
#实例化执行器类
br = BeautifulReport(suites=su)
#执行测试用例收集测试报告
br.report(description="接口测试报告",filename="test.html")

二、拓展(三元运算)
filename="test"
res = filename  if filename.endswith('.html') else filename + '.html'

def test(filename):
    if filename.endswith('.html'):
        return filename
    else:
        return filename + '.html'


三、unittestreport生成测试报告
1、安装unittestreport
pip install unittestreport
2、代码
import unittest
from unittestreport import TestRunner
#创建测试套件：用来收集测试用例
su = unittest.defaultTestLoader.discover(start_dir=".", pattern='demo*.py')
runner = TestRunner(
                 suite=su,
                 filename="py52report.html",
                 report_dir="./reports",
                 title='接口测试报告',
                 tester='海励',
                 desc="上课项目测试生成的报告",
                 templates=2
                    )
runner.run()



import unittest
from unittestreport import TestRunner

#创建测试套件：用来收集测试用例
su = unittest.defaultTestLoader.discover(start_dir=".", pattern='demo*.py')


runner = TestRunner(
                 suite=su,
                 filename="py52report.html",
                 report_dir="./reports",
                 title='接口测试报告',
                 tester='海励',
                 desc="上课项目测试生成的报告",
                 templates=2
                    )

runner.run()

"""
import unittest
import unittestreport

su = unittest.defaultTestLoader.discover(start_dir='.', pattern="demo*.py")
runner = unittestreport.TestRunner(
        suite=su,
        title="测试报告",
        report_dir="./report_dir",
        filename="zhangsan.html",
        tester="tom",
        desc="happy"
)

runner.run()




