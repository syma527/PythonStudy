"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/10/19 21:22
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
三、鼠标操作
1、导入包  
	from selenium.webdriver.common.action_chains import ActionChains
	from selenium.webdriver import ActionChains
2、使用
    执行原理：将actions将鼠标的动作都收集到一个list中，在调用perform()的时候才会去执行鼠标操作
	1、实例化
		actions = ActionChains(driver)
	2、鼠标移动      
		actions.move_to_element(menu)
	3、鼠标点击  
		action.click(ele2)           
	4、鼠标长按
		action.click_and_hold(on_element=ele2)    
	5、鼠标释放
		action.release(ele2)              
	6、鼠标暂停操作(秒)
		action.pause(5)                                   
	7、执行鼠标操作方法
		actions.perform()
		
	
3、链式调用
	ActionChains(driver).move_to_element(element_obj1).click(element_obj2).perform()
4、案例
	1、鼠标移动
		https://www.runoob.com/js/js-htmldom-events.html  
	2、鼠标移动
		https://www.runoob.com/try/try.php?filename=tryjs_events_mouseover
    3、鼠标移动点击
		https://www.runoob.com/try/try.php?filename=trydhtml_event_onclick2
	4、鼠标长按               
		https://www.runoob.com/try/try.php?filename=trydhtml_event_onmousedown 


"""

# 鼠标移动
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains

import time
from selenium import webdriver
dr = webdriver.Chrome()
dr.get(url="https://www.runoob.com/try/try.php?filename=tryjs_events_mouseover")
dr.maximize_window()

dr.implicitly_wait(5)
action = ActionChains(driver=dr)
dr.switch_to.frame('iframeResult')
time.sleep(5)
ele = dr.find_element_by_xpath('//div[@onmouseover="mOver(this)"]')
#收集命令
action.move_to_element(to_element=ele)
#执行命令
action.perform()

# action.click()







