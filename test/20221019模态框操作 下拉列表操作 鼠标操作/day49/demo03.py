"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/10/19 20:39
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
三、div+p标签的下拉框
1、通过元素定位来处理

2、场景
设置 --- 高级搜索 --- 文档格式 --- 触发下拉列表 --- 找到所有下拉选项

"""
import time
from selenium import webdriver
dr = webdriver.Chrome()
dr.get(url="https://www.baidu.com/")
dr.maximize_window()
dr.implicitly_wait(5)

#设置
dr.find_element_by_xpath('//span[text()="设置"]').click()
#高级搜索
#拿到3个span标签对象
eles = dr.find_elements_by_xpath('//div[@id="s-user-setting-menu"]/div[@class="s-user-setting-pfmenu"]/a/span')
time.sleep(3)
for element in eles:
    if element.text == "高级搜索":
        element.click()

#触发下拉框
dr.find_element_by_xpath('//div[@class="c-select adv-ft-select"]').click()

#定位到你需要的下选项,再点击
eles2 = dr.find_elements_by_xpath('//span[@id="adv-setting-ft"]//div[@class="c-select-dropdown-list"]/p')
print("="*30)
for element in eles2:
    print(element,element.text)
    if element.text == "微软 Powerpoint (.ppt)":
        element.click()
