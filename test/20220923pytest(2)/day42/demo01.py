"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/9/23 19:56
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""



import pytest
@pytest.fixture(scope="function")
def init_login1():
    print("\ninit_login1前置条件")
    yield "success"
    print("\ninit_login1后置处理")

@pytest.fixture(scope="class")
def init_login2():
    print("\ninit_login2前置条件")
    yield "success"
    print("\ninit_login2后置处理")


@pytest.mark.usefixtures("init_login1")
@pytest.mark.usefixtures("init_login2")
def test_01(init_login1):
    print("测试用例1")
    test_str = init_login1
    print("参数的使用",test_str)


class TestDemo:
    @pytest.mark.usefixtures("init_login2")
    def test_03(self,init_login2):
        demo = init_login2
        print(demo)




