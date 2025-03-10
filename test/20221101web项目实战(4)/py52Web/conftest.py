"""
============================
Project: py52Web
Author:柠檬班-海励
Time:2022/10/24 20:17
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""


"""
前后置放这里

"""
from tools.handle_remove_file import HandleRemoveFile
from page.manage.page1_login_page import LoginPage
from page.manage.page2_home_page import HomePage
from page.manage.page3_add_product import AddProduct



import time
import pytest
from selenium import webdriver

#管理端的前置后置
@pytest.fixture(scope="class")
def manage_setup_tear_down():
    HandleRemoveFile.remove_file()
    driver = webdriver.Chrome()
    driver.get(url="http://mall.lemonban.com/admin/#/login")
    driver.maximize_window()
    login_page = LoginPage(driver=driver)
    home_page = HomePage(driver=driver)
    product_page = AddProduct(driver=driver)
    yield driver,login_page,home_page,product_page
    time.sleep(20)
    driver.quit()












