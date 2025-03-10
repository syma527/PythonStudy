"""
============================
Project: py52Web
Author:柠檬班-海励
Time:2022/10/24 21:22
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
将page页面的行为组织起来就是我们的测试用例

"""

import pytest

@pytest.mark.usefixtures("manage_setup_tear_down")
class TestAddProduct:
    def test_add_product(self,manage_setup_tear_down):
        driver,login_page = manage_setup_tear_down
        login_page.manage_login(user="student",password="123456a")






