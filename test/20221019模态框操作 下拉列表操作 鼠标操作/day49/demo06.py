"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/10/19 21:54
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""

长按鼠标

"""
from selenium.webdriver import ActionChains
import time
from selenium import webdriver
dr = webdriver.Chrome()
dr.get(url="https://www.runoob.com/try/try.php?filename=trydhtml_event_onmousedown")
dr.maximize_window()
dr.implicitly_wait(3)
action = ActionChains(driver=dr)
dr.switch_to.frame('iframeResult')
time.sleep(2)
ele = dr.find_element_by_xpath('//img[@id="myimage"]')
#收集命令
action.move_to_element(to_element=ele)
#长按鼠标左键
action.click_and_hold(on_element=ele)
#暂停执行
action.pause(5)
#释放按键
action.release(ele)
#执行命令
action.perform()


# action.click()