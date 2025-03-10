"""
============================
Project: py52Web
Author:柠檬班-海励
Time:2022/10/24 20:21
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""


"""
HomePage页面最主要的就是菜单的管理
切换需要的菜单
# 菜单栏一级菜单
first_menu_product = {'loc': (By.XPATH, f'//div[@class="el-submenu__title"]/span[text()="{first_menu_name}"]'), 'page_action': f'{first_menu_name}一级菜单'}
        
# 菜单栏二级菜单
second_menu_product = {'loc': (By.XPATH, f'//li[@role="menuitem"]/span[text()="{second_menu_name}"]'), 'page_action': f'二级菜单{second_menu_name}'}

"""

from tools.base_page import BasePage


from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self,driver):
        #元素操作
        self.base = BasePage(driver=driver)

    #切换菜单
    def switch_menu(self,first_menu_name,second_menu_name):
        #一级菜单定位表达式(通用的)
        first_menu_product = {'loc': (By.XPATH, f'//div[@class="el-submenu__title"]/span[text()="{first_menu_name}"]'), 'page_action': f'一级菜单{first_menu_name}'}
        #二级菜单定位表达式(通用的)
        second_menu_product = {'loc': (By.XPATH, f'//li[@role="menuitem"]/span[text()="{second_menu_name}"]'), 'page_action': f'二级菜单{second_menu_name}'}
        #选择一级菜单
        self.base.find_element_and_click(locations=first_menu_product["loc"],page_action=first_menu_product["page_action"])
        #选择二级菜单
        self.base.find_element_and_click(locations=second_menu_product["loc"],page_action=second_menu_product["page_action"])






