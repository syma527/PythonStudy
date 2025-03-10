"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/10/19 20:09
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、模态框
1、元素定位方式进行处理


"""

import time
from selenium import webdriver



dr = webdriver.Chrome()
dr.get(url="https://www.w3school.com.cn/tiy/t.asp?s=h&f=bs_modal")
dr.implicitly_wait(10)
dr.switch_to.frame('iframeResult')
dr.find_element_by_xpath('//button[contains(text(),"打开")]').click()
time.sleep(5)
dr.find_element_by_xpath('//button[contains(text(),"关闭")]').click()


















