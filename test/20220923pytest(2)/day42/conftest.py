"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/9/23 20:42
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
全局的前后置文件

"""
import pytest
@pytest.fixture(scope="class")
def init_class():
    num1 = 100
    num2 = 200
    yield num1,num2
    print("后置处理")