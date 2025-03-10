"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/9/26 20:41
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
import pytest

@pytest.mark.py56
@pytest.mark.login
def test_08():
    print('test_08')

@pytest.mark.py56
def test_09():
    print('test_09')

@pytest.mark.login
def test_10():
    print('test_10')

def test_11():
    print('test_11')