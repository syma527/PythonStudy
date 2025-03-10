"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/9/23 21:43
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""

import pytest

@pytest.mark.usefixtures("init_func")
def test_01():
    print("demo02的test_01")

if __name__ == '__main__':
    pytest.main(['-sv'])

