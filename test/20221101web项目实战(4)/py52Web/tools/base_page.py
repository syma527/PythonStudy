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

    def __wait_elements_located(self,locations,page_action,in_dom=None):
        if in_dom == 1:
            #只要加载到dom树中就可以，不一定可见
            elements = self.wait.until(EC.presence_of_all_elements_located(locator=locations))
        else:
        #元素加载且可见(有尺寸能在屏幕上看到的),返回多个元素
            elements = self.wait.until(EC.visibility_of_all_elements_located(locator=locations))
        return elements

    #等待元素可点击
    def __wait_element_clickable(self,locations,page_action):
        element = self.wait.until(EC.element_to_be_clickable(locator=locations))
        time.sleep(1)
        return element

    #=================================================

    #获取元素，然后输出值
    def find_element_and_sendkeys(self,locations,page_action,value):
        try:
            ele = self.__wait_element_located(locations=locations,page_action=page_action)
            ele.clear()
            ele.click()
            ele.send_keys(value)
        except Exception as e:
            print("执行__wait_element_located报错")
            #截图
            self.save_screenshot(page_action=page_action)

    #给输入框赋值
    def element_send_keys(self,element,value):
        element.send_keys(value)

    #获取元素，然后点击
    def find_element_and_click(self,locations,page_action):
        try:
            ele = self.__wait_element_located(locations=locations,page_action=page_action)
            ele.click()
        except Exception as e:
            print("执行find_element_and_click报错")
            #截图
            self.save_screenshot(page_action=page_action)

    #获取多个元素，返回list
    def find_more_element(self,locations, page_action,in_dom=None):
        elements = self.__wait_elements_located(locations=locations, page_action=page_action,in_dom=in_dom)
        return elements

    #等待元素可点击，然后再点击
    def find_element_clickable_and_click(self,locations,page_action):
        element = self.__wait_element_clickable(locations=locations,page_action=page_action)
        element.click()


    #切换进入iframe
    def switch_iframe(self,locations,page_action,name=None,iframe_index=0,in_dom=None):
        if name:
            #通过name或者id来定位
            self.driver.switch_to.frame(name)
        else:
            #通过xpath元素定位来切换iframe
            elements = self.__wait_elements_located(locations=locations, page_action=page_action,in_dom=in_dom)
            self.driver.switch_to.frame(elements[iframe_index])

    #从iframe切换到最外层
    def switch_out_iframe(self):
        self.driver.switch_to.default_content()

    #错误截图方法
    def save_screenshot(self,page_action):
        print("开始截图")
        #error_image_dir = D:\vip_class\py52Web\error_images\page_action时间.png
        png_name = time.strftime("%Y%m%d_%H%M%S",time.localtime())
        name = os.path.join(error_image_dir,f"{page_action}{png_name}.png")
        self.driver.save_screenshot(filename=name)






