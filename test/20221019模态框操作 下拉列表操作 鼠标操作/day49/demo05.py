"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/10/19 21:49
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""

"""
鼠标点击

"""
from selenium.webdriver import ActionChains

import time
from selenium import webdriver
dr = webdriver.Chrome()
dr.get(url="https://www.runoob.com/try/try.php?filename=trydhtml_event_onclick2")
dr.maximize_window()

dr.implicitly_wait(3)
action = ActionChains(driver=dr)
dr.switch_to.frame('iframeResult')
time.sleep(2)
ele = dr.find_element_by_xpath('//h1[contains(text(),"点击文本")]')
#收集命令
action.move_to_element(to_element=ele)
#点击
action.click(on_element=ele)
#执行命令
action.perform()

# action.click()


