"""
============================
Project: py52Web
Author:柠檬班-海励
Time:2022/10/26 20:47
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
from tools.handle_path import image_dir
from tools.base_page import BasePage


import time
import pyautogui
from selenium.webdriver.common.by import By




class AddProduct:
    #1、点新增按钮
    add_button = {'loc': (By.XPATH, '//button[@class="el-button el-button--primary el-button--small"]/span[text()="新增"]'), 'page_action': '点新增'}
    #2、点商品图片,触发图片上传模态框
    product_image = {'loc': (By.XPATH, '//li[@class="el-upload-list__item"]/div[@tabindex="0" and @class = "el-upload el-upload--picture-card"]'), 'page_action': '点商品图片加号'}

    # 3、切换选项卡,点上传图片
    #switch_table = {'loc': (By.XPATH, '//div[@role="tablist"]/div[text()="{}"]'), 'page_action': '切换到'}

    # 4、点+图片上传，打开添加图片窗口，再从本地选择图片上传
    open_upload_window = {'loc': (By.XPATH, '//div[@class="upload-img-preview"]/div[@class="el-upload el-upload--picture-card"]'), 'page_action': '打开图片上传窗口'}

    def __init__(self,driver):
        #元素操作
        self.base = BasePage(driver=driver)

    #点新增
    def click_add(self):
        self.base.find_element_and_click(locations=self.add_button["loc"],page_action=self.add_button["page_action"])

    #点商品图片,触发图片上传模态框
    def click_product_image(self):
        self.base.find_element_and_click(locations=self.product_image["loc"],page_action=self.product_image["page_action"])


    #切换到上传图片选项卡页面
    #切换到上传文件，切换到选择文件通用方法
    def switch_card(self,card_name):
        switch_table = {'loc': (By.XPATH, f'//div[@role="tablist"]/div[text()="{card_name}"]'), 'page_action': f'切换到{card_name}'}
        self.base.find_element_and_click(locations=switch_table["loc"],page_action=switch_table["page_action"])


    #点+图片上传，打开添加图片窗口，再从本地选择图片上传
    def upload_product_image(self):
        self.base.find_element_and_click(locations=self.open_upload_window["loc"], page_action=self.open_upload_window["page_action"])
        time.sleep(1)
        pyautogui.typewrite(image_dir)
        time.sleep(1)
        pyautogui.press(keys='ENTER',presses=3)
