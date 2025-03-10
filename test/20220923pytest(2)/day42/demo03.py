"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/9/23 21:22
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""

全局共享文件conftest.py(可以理解为全局变量)


"""
import pytest


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


