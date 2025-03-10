"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/9/21 21:26
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
前后置(夹具)

unittest:
1、函数级别：setup、teardown
2、类级别(类方法)：setupClass、teardownClass

pytest【了解】:
模块级别(py文件)：
setup_module: 模块中第一个测试用例执行之前执行一次
teardown_module: 模块中最后一个测试用例执行之后执行一次

函数级别:
setup_function: 每个测试用例执行之前执行一次
teardown_function: 每个测试用例执行之后执行一次
只对类外面的测试函数生成，类里面的测试用是不生效的

类级别:
setup_class: 每个测试类执行之前执行一次
teardown_class: 每个测试类执行之后执行一次
只对类里面的测试用例生效，类外面的不生效


fixture前置【掌握】



"""

import pytest

#autouse=True 自动调用前后置
#scope="function" 设置前后置的级别
# @pytest.fixture(scope="function",autouse=True)
@pytest.fixture
def setup_demo():
    print("\n测试用例前置")
    # cls.header = {"locale": "zh_CN"}
    # cls.replace = HandleReplace()
    # cls.response = HandleResponse()
    # cls.extract = HandleExtractData()
    # cls.request = HandleRequest()
    # cls.assert_db = HandleAssertDb()
    yield "header","replace",
    print("\n测试用例的后置")

@pytest.mark.usefixtures("setup_demo")
def test_01(setup_demo):
    header,replace = setup_demo
    print(header,replace)
    #测试用例执行逻辑
    print("\n测试用例执行逻辑")

# if __name__ == '__main__':
#     pytest.main(['-s','-v'])

