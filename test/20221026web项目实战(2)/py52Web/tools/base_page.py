"""
============================
Project: py52Web
Author:柠檬班-海励
Time:2022/10/24 20:29
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""


"""
错误重试
http://testingpai.com/article/1617701836265


元素操作的方法

dr = webdriver.Chrome()
dr.find_element()

"""


from tenacity import *
from tools.handle_path import error_image_dir


import time
import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self,driver:webdriver.Chrome):
        #获取传入的webdriver
        self.driver = driver
        #实例化显示等待
        self.wait = WebDriverWait(driver=driver,timeout=10)
        self.retry_count = 0

    #等待元素出现，定位到元素，返回元素对象
    @retry(stop=stop_after_attempt(3))
    def __wait_element_located(self,locations,page_action):
        try:
            #locations: 传入元组
            #输入元素表达式
            #需要等待
            time.sleep(1.6) #如果元素定位报错，可以尝试加强制等待试试
            element = self.wait.until(EC.visibility_of_element_located(locator=locations))
        except Exception as e:
            self.retry_count += 1
            if self.retry_count == 3:
                print("执行__wait_element_located报错")
                #截图
                self.save_screenshot(page_action=page_action)
                self.retry_count = 0
            else:
                print("继续重复执行该步骤")
        else:
            self.retry_count = 0
            return element

    #获取元素，然后输出值
    def find_element_and_sendkeys(self,locations,value,page_action):
        try:
            ele = self.__wait_element_located(locations=locations,page_action=page_action)
            ele.send_keys(value)
        except Exception as e:
            print("执行__wait_element_located报错")
            #截图
            self.save_screenshot(page_action=page_action)

    #获取元素，然后点击
    def find_element_and_click(self,locations,page_action):
        try:
            ele = self.__wait_element_located(locations=locations,page_action=page_action)
            ele.click()
        except Exception as e:
            print("执行find_element_and_click报错")
            #截图
            self.save_screenshot(page_action=page_action)

    #错误截图方法
    def save_screenshot(self,page_action):
        print("开始截图")
        #error_image_dir = D:\vip_class\py52Web\error_images\page_action时间.png
        png_name = time.strftime("%Y%m%d_%H%M%S",time.localtime())
        name = os.path.join(error_image_dir,f"{page_action}{png_name}.png")
        self.driver.save_screenshot(filename=name)






