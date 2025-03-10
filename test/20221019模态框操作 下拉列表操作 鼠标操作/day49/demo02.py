"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/10/19 20:21
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""

"""
二、select下拉框选择
3、使用步骤
    1、定位select元素
    2、将定位到的select元素转成select对象
        sel = Select(定位的元素对象)
    3、选择下拉框
         1、通过索引选择下拉选项，索引从0开始
            sel.select_by_index(index)
         2、通过value属性选择下拉选项
            sel.select_by_value(value)
         3、文本内容选择下拉选项
            sel.select_by_visible_text(text)

"""
import time
from selenium.webdriver.support.select import Select
from selenium import webdriver
dr = webdriver.Chrome()
dr.get(url="https://www.w3school.com.cn/tiy/t.asp?f=eg_html_elements_select")
dr.implicitly_wait(5)
dr.switch_to.frame('iframeResult')
ele = dr.find_element_by_xpath('//select[@name="cars"]')
sel = Select(ele)
#通过index获取value值进行选择,索引从0开始
time.sleep(3)
sel.select_by_index(1)
time.sleep(3)
sel.select_by_value("audi")
time.sleep(3)
sel.select_by_visible_text(text="Fiat")









