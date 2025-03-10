"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/10/21 19:58
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
from selenium.webdriver import ActionChains

import time
from selenium import webdriver
dr = webdriver.Chrome()
dr.get(url="https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
dr.maximize_window()

dr.implicitly_wait(3)
action = ActionChains(driver=dr)
dr.switch_to.frame('iframeResult')
time.sleep(2)

source = dr.find_element_by_xpath('//div[@id="draggable"]')
target = dr.find_element_by_xpath('//div[@id="droppable"]')
#收集命令
action.drag_and_drop(source=source,target=target)

#执行命令
action.perform()



