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
元素操作的方法

dr = webdriver.Chrome()
dr.find_element()

"""
from tools.handle_path import error_image_dir


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self,driver:webdriver.Chrome):
        #获取传入的webdriver
        self.driver = driver
        #实例化显示等待
        self.wait = WebDriverWait(driver=driver,timeout=10)

    #等待元素出现，定位到元素，返回元素对象
    def __wait_element_located(self,locations):
        #locations: 传入元组
        #输入元素表达式
        #需要等待
        element = self.wait.until(EC.visibility_of_element_located(locator=locations))
        return element

    #获取元素，然后输出值
    def find_element_and_sendkeys(self,locations,value):
        ele = self.__wait_element_located(locations=locations)
        ele.send_keys(value)

    #获取元素，然后点击
    def find_element_and_click(self,locations):
        ele = self.__wait_element_located(locations=locations)
        ele.click()




    #错误截图方法
    def save_screenshot(self,page_action):
        #下次课继续讲
        #error_image_dir
        self.driver.save_screenshot(filename=error_image_dir)






