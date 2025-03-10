"""
============================
Project: py52Web
Author:柠檬班-海励
Time:2022/10/24 20:20
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""

from tools.base_page import BasePage


from selenium.webdriver.common.by import By


"""
# 用户名输入框
user_input = {'loc': (By.XPATH, '//input[@placeholder="用户名"]'), 'page_action': '登陆页面用户输入框'}
# 密码输入框
password_input = {'loc': (By.XPATH, '//input[@placeholder="密码"]'), 'page_action': '登陆页面密码输入框'}
# 验证码输入框
code_input = {'loc': (By.XPATH, '//input[@placeholder="验证码"]'), 'page_action': '登陆页面验证码输入框'}
# 登陆按钮
login_input = {'loc': (By.XPATH, '//input[@value="登录"]'), 'page_action': '登陆页面登陆按钮'}


"""


class LoginPage:
    # 用户名输入框
    user_input  = {'loc': (By.XPATH, '//input[@placeholder="用户名"]'), 'page_action': '登陆页面用户输入框'}
    # 密码输入框
    password_input = {'loc': (By.XPATH, '//input[@placeholder="密码"]'), 'page_action': '登陆页面密码输入框'}
    # 验证码输入框
    code_input = {'loc': (By.XPATH, '//input[@placeholder="验证码"]'), 'page_action': '登陆页面验证码输入框'}
    # 登陆按钮
    login_input = {'loc': (By.XPATH, '//input[@value="登录"]'), 'page_action': '登陆页面登陆按钮'}

    def __init__(self,driver):
        self.base = BasePage(driver=driver)

    #管理端登陆,工具类
    def manage_login(self,user,password):
        #定位到用户名输入框，输入账号
        self.base.find_element_and_sendkeys(locations=self.user_input["loc"],value=user,page_action=self.user_input["page_action"])
        #定位到密码输入框，输入密码
        self.base.find_element_and_sendkeys(locations=self.password_input["loc"],value=password,page_action=self.password_input["page_action"])
        #定位到验证码输入框，输入验证码
        self.base.find_element_and_sendkeys(locations=self.code_input["loc"],value="lemon",page_action=self.code_input["page_action"])
        #定位到登陆按钮，去点击
        self.base.find_element_and_click(locations=self.login_input["loc"],page_action=self.login_input["page_action"])


if __name__ == '__main__':
    from selenium import webdriver
    dr = webdriver.Chrome()
    dr.get(url="http://mall.lemonban.com/admin/#/login")
    cl = LoginPage(dr)
    cl.manage_login(user="student",password="123456a")

    # dr.save_screenshot()

