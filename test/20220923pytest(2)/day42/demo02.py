"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/9/23 20:44
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
用例参数换
1、函数用例的参数化
2、类用例的参数化


import pytest
case_list = [
             {"id":"1","url":"https://www.ketangpai.com1"},
             {"id":"2","url":"https://www.ketangpai.com2"},
             {"id":"3","url":"https://www.ketangpai.com3"},
             {"id":"4","url":"https://www.ketangpai.com4"},
           ]
@pytest.mark.parametrize("case",case_list)
def test_04(case):
    print("test_04")
    print(case)
if __name__ == '__main__':
    pytest.main(['-sv'])




import pytest
case_list = [
             {"id":"1","url":"https://www.ketangpai.com1"},
             {"id":"2","url":"https://www.ketangpai.com2"},
             {"id":"3","url":"https://www.ketangpai.com3"},
             {"id":"4","url":"https://www.ketangpai.com4"},
           ]
class TestDemo:
    @pytest.mark.parametrize("case", case_list)
    def test_05(self,case):
        print("测试数据:",case)
if __name__ == '__main__':
    pytest.main(['-sv'])
    
    
import pytest

#夹具==前后置  yield 与 return
# @pytest.fixture(scope="function")
@pytest.fixture(scope="class")
def init_class():
    num1 = 100
    num2 = 200
    yield num1,num2
    print("后置处理")
case_list = [
             {"id":"1","url":"https://www.ketangpai.com1"},
             {"id":"2","url":"https://www.ketangpai.com2"},
             {"id":"3","url":"https://www.ketangpai.com3"},
             {"id":"4","url":"https://www.ketangpai.com4"},
           ]
@pytest.mark.usefixtures('init_class')
class TestDemo:
    @pytest.mark.parametrize("case", case_list)
    def test_05(self,case,init_class):
        print("测试数据:",case)
        num1,num2 = init_class
        print('前置返回的数据:',num1,num2)

if __name__ == '__main__':
    pytest.main(['-sv'])
    
"""


"""
import pytest

#夹具==前后置  yield 与 return
# @pytest.fixture(scope="function")
@pytest.fixture(scope="class")
def init_class():
    num1 = 100
    num2 = 200
    yield num1,num2
    print("后置处理")
case_list = [
             {"id":"1","url":"https://www.ketangpai.com1"},
             {"id":"2","url":"https://www.ketangpai.com2"},
             {"id":"3","url":"https://www.ketangpai.com3"},
             {"id":"4","url":"https://www.ketangpai.com4"},
           ]
@pytest.mark.usefixtures('init_class')
class TestDemo:
    @pytest.mark.parametrize("case", case_list)
    def test_05(self,case,init_class):
        print("测试数据:",case)
        num1,num2 = init_class
        print('前置返回的数据:',num1,num2)

if __name__ == '__main__':
    pytest.main(['-sv'])
"""











