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
from page.manage.page2_home_page import HomePage


import pytest

@pytest.mark.usefixtures("manage_setup_tear_down")
class TestAddProduct:
    def test_add_product(self,manage_setup_tear_down):
        #前置初始化浏览器，打开后端网站
        driver,login_page,home_page,product_page = manage_setup_tear_down
        #登陆
        login_page.manage_login(user="student",password="123456a")
        #切换到产品管理页面
        home_page.switch_menu(first_menu_name="产品管理",second_menu_name="产品管理")
        #点新增
        product_page.click_add()
        #点商品图片,触发图片上传模态框
        product_page.click_product_image()
        #切换到上传图片选项卡
        product_page.switch_card(card_name="上传图片")
        #上传本地图片
        product_page.upload_product_image()









