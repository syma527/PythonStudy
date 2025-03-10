"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/10/10 20:20
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、元素定位
1、id --- 唯一(相对来说)，id绑定了很多js代码,不会变动，稳定性好
dr.find_element_by_id()
2、class --组合使用,不唯一，但是可以和其他属性组合起来唯一 
dr.find_element_by_class_name()
3、css -- 不用
dr.find_element_by_css_selector()
4、xpath -- 通过路径定位
   1、绝对路径：/html/body/div[1]/div[2]/div[5]/div[1]/div/form/span[1]/input
   2、相对路径：//*[@id="kw"] --常用
dr.find_element_by_xpath()
5、通过标签名称定位 -- 不用
dr.find_element_by_tag_name()
6、name属性 -- 不用
dr.find_element_by_name()
7、链接文本定位[精准匹配链接文本内容] -- 不用
dr.find_element_by_link_text()
8、链接文本定位[模糊匹配链接文本内容] -- 不用
dr.find_element_by_partial_link_text()


二、重点掌握
1、id
2、class
3、xpath(相对路径)
"""

import time
from selenium import webdriver

dr = webdriver.Chrome(r'D:\chromeDriver\105\chromedriver.exe')
dr.get(url="https://www.baidu.com/")
time.sleep(1)
#id属性定位元素
# ele = dr.find_element_by_id("kw")

#class属性值来定位
# ele = dr.find_element_by_class_name("s_ipt")

#css定位元素
# ele = dr.find_element_by_css_selector("#kw")

#xpath定位元素
# ele = dr.find_element_by_xpath('//input[@class="s_ipt"]')
# ele = dr.find_element_by_xpath('/html/body/div[1]/div[2]/div[5]/div[1]/div/form/span[1]/input')

#name属性定位
ele = dr.find_element_by_name('wd')

time.sleep(1)

ele.send_keys('py52期')
time.sleep(10)
dr.quit()


#标签名称
# dr.find_element_by_tag_name()
#name属性定位
# dr.find_element_by_name()
#链接文本定位[精准匹配链接文本内容]
# dr.find_element_by_link_text()
#链接文本定位[模糊匹配链接文本内容]
# dr.find_element_by_partial_link_text()




