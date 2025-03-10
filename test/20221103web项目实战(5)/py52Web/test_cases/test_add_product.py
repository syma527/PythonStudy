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
        #点击上传
        product_page.confirm_upload()
        #切换到上传图片选项卡
        product_page.switch_card(card_name="选择图片")
        #选择一个图片，点确定
        product_page.find_images_and_click()
        #选择产品下拉列表
        product_page.product_list()
        #选择产品分组
        product_page.product_group()
        #设置产品库存信息
        product_page.stock_set()
        #物流信息设置
        product_page.freight_set()
        #设置产品信息
        product_page.pro_info()
        #设置产品详情
        product_page.product_descriptions()
        #确认添加产品
        product_page.product_add_confirm()
        #断言
        product_page.assert_product()








        #删除错误截图 + 断言 +  验证码解析 +




#深浅拷贝 + 装饰器的使用(封装错误重试和截图)

#测试报告

#毕业典礼计划是周六  满勤 + 作业提交



