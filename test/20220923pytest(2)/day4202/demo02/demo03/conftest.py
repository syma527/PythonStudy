"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/9/23 21:45
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
import pytest

@pytest.fixture(scope="function")
def init_func():
    print("\n前置条件2023")
    yield
    print("后置清理2023")