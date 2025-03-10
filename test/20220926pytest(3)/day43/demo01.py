"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/9/26 20:11
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、用例收集
1、自动收集用例
2、指定收集测试用例(文件)
3、标记测试用例

二、标记的使用
1、conftest.py 用来写前置后置的文件
2、pytest.ini  pytest的配置文件，用来写标签的

三、pytest.ini语法
1、pytest.ini文件名必须是这样写，不能随便写
2、基本模板，[pytest]和markers= 固定这么写的，不能改
[pytest]
markers=
    py52:python52_pytest
    py56:python56_pytest  
3、不能写注释，不支持写注释
4、对单个测试用例进行打标签
@pytest.mark.login
def test_02():
    print("test_02")

5、对整个测试类进行打标签
@pytest.mark.login
class TestDemo:
    def test_03(self):
        print("test_03")

    def test_04(self):
        print("test_04")
        
6、通过pytestmark类属性的方式实现给整个类打标签
给整个测试用例类里面的所有测试用例打标签
pytestmark这个类属性名称不能改
class TestDemo:
    pytestmark=[pytest.mark.login,pytest.mark.py56]

    def test_03(self):
        print("test_03")

    def test_04(self):
        print("test_04")
7、给用例或者类打多个标签
执行的时候标签是不冲突的，只要打了某个标签，指定执行的时候就会执行
@pytest.mark.py56
@pytest.mark.login
def test_05():
    print('test_05')
@pytest.mark.py56
def test_06():
    print('test_06')  
    
@pytest.mark.login
@pytest.mark.py56
class TestDemo:
    def test_03(self):
        print("test_03")
    def test_04(self):
        print("test_04") 
        
"""
import pytest


# def test_01():
#     print("test_01")
# @pytest.mark.login
# def test_02():
#     print("test_02")



# @pytest.mark.login
# class TestDemo:
#     def test_03(self):
#         print("test_03")
#     def test_04(self):
#         print("test_04")


class TestDemo:
    #给整个测试用例类里面的所有测试用例打标签
    #pytestmark=[pytest.mark.login,pytest.mark.py56]
    # pytestmark=[pytest.mark.login]

    def test_01(self):
        print("test_01")
        assert 1==2

    def test_02(self):
        print("test_02")

    def test_03(self):
        print("test_03")

    def test_04(self):
        print("test_04")