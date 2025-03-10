"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/10/21 21:35
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
文件上传
//span[@class="soutu-btn"]
//input[@class="upload-pic"]

安装第三方包
pip install  pywinauto==0.6.8


1、pywinauto文件上传     
	1、安装
		 pip install pywinauto    
	2、使用 
    		from pywinauto.keyboard import send_keys
    		send_keys('文件路径1')
    		send_keys('文件路径2')
    		send_keys('{ENTER}')
	3、特点
		1、仅支持windows
		2、支持多文件上传
		3、文件路径不能有中文
		4、等待弹框完成之后再send_keys                                                         
	4、案例
		1、https://www.baidu.com
		2、百度搜图  


"""
import time
from selenium import webdriver
from pywinauto.keyboard import send_keys

dr = webdriver.Chrome()
dr.get("https://www.baidu.com")
dr.implicitly_wait(5)
dr.find_element_by_xpath('//span[@class="soutu-btn"]').click()
dr.find_element_by_xpath('//input[@class="upload-pic"]').click()
#先等待windows窗口打开再去赋值
time.sleep(3)
send_keys(keys=r'D:\py52.png')
send_keys(keys='{ENTER}')










