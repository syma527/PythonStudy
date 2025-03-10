"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/10/21 21:11
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
2、将元素显示到可视区域
	1、方式一、元素本身方法，将元素显示到可视区域
		element.location_once_scrolled_into_view
	2、js操作元素,定位元素滚动到可视区域 
        与窗口顶端对齐,只要元素在页面就可以用,不管元素所属哪个滚动条
		driver.execute_script("arguments[0].scrollIntoView(true)",elem) 
		与窗口底部对齐,只要元素在页面就可以用,不管元素所属哪个滚动条
		driver.execute_script("arguments[0].scrollIntoView(false)",elem)  


"""

from selenium.webdriver.common.keys import Keys

from selenium import webdriver
dr = webdriver.Chrome()
dr.get("https://www.baidu.com")
dr.implicitly_wait(5)
dr.find_element_by_xpath('//input[@id="kw"]').send_keys("柠檬班",Keys.ENTER)
ele = dr.find_element_by_xpath('//div[contains(text(),"相关搜索")]')

#通过webEmement方法实现
# ele.location_once_scrolled_into_view

import time
time.sleep(3)
#通过js实现

# dr.execute_script("arguments[0].scrollIntoView(true)",ele)
dr.execute_script("arguments[0].scrollIntoView(false)",ele)






