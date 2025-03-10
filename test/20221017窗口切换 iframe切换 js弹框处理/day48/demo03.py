"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/10/17 20:06
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
三、弹框处理
1、js弹框
Alert类处理js弹框
获取文本内容
text = alert.text

点确定(alert.accept())
import time
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
dr = webdriver.Chrome()
dr.get("https://www.w3school.com.cn/tiy/t.asp?f=eg_js_alert")
dr.implicitly_wait(5)
alert = Alert(driver=dr)
dr.switch_to.frame('iframeResult')
dr.find_element_by_xpath('//button[text()="试一试"]').click()
#获取文本内容
text = alert.text
print(text)
time.sleep(5)
#点确定
alert.accept()


点取消(alert.dismiss()):
import time
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
dr = webdriver.Chrome()
dr.get("https://www.w3school.com.cn/tiy/t.asp?f=eg_js_confirm")
dr.implicitly_wait(5)
alert = Alert(driver=dr)
dr.switch_to.frame('iframeResult')
dr.find_element_by_xpath('//button[text()="试一试"]').click()
#获取文本内容
text = alert.text
print(text)
time.sleep(5)
#点取消
alert.dismiss()


弹框输入文本内容:
import time
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
dr = webdriver.Chrome()
dr.get("https://www.w3school.com.cn/tiy/t.asp?f=eg_js_prompt")
dr.implicitly_wait(5)
alert = Alert(driver=dr)
dr.switch_to.frame('iframeResult')
dr.find_element_by_xpath('//button[text()="试一试"]').click()
#获取文本内容
text = alert.text
print(text)
time.sleep(5)
#输入文本内容，看不到输入效果
alert.send_keys("py52")
alert.accept()

2、模态框
元素定位可以搞定

3、下拉菜单
4、鼠标操作
5、按键操作
6、js滚动 
7、文件上传
8、web自动化项目(po)

"""
import time
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
dr = webdriver.Chrome()
dr.get("https://www.w3school.com.cn/tiy/t.asp?f=eg_js_prompt")
dr.implicitly_wait(5)
alert = Alert(driver=dr)
dr.switch_to.frame('iframeResult')
dr.find_element_by_xpath('//button[text()="试一试"]').click()
#获取文本内容
text = alert.text
print(text)
time.sleep(5)
#输入文本内容，看不到输入效果
alert.send_keys("py52")
alert.accept()




