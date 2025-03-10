"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/10/21 21:51
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""

"""
2、pyautogui文件上传                 
	1、安装
		pip install pyautogui             
	2、使用
		import pyautogui 
		pyautogui.typewrite(r'D:\88.png') 
		pyautogui.press(keys='ENTER',presses=3)   
         参数：
         1、keys：按键; 
         2、presses=1：重复按多少次; 
         3、interval=0.0：间隔（浮动，可选）：每次按下之间的秒数
	3、特点
		1、跨平台可用(linux、windows、mac)
		2、不支持多文件上传                            	
		3、 keys命令不区分大小写
		4、文件路径不能有中文
		5、输入法未切换为英文模式需要多按几次 
		6、mac环境下使用pyautogui点击无效
	4、案例
        	1、https://www.baidu.com
		    2、百度搜图
"""
import time
from selenium import webdriver
import pyautogui
dr = webdriver.Chrome()
dr.get("https://www.baidu.com")
dr.implicitly_wait(5)
dr.find_element_by_xpath('//span[@class="soutu-btn"]').click()
dr.find_element_by_xpath('//input[@class="upload-pic"]').click()
#先等待windows窗口打开再去赋值
time.sleep(3)
pyautogui.typewrite(r'D:\py52.png')
#需要按次，第一次回车是给输入法的,第二次是给windows窗口
pyautogui.press(keys='ENTER',presses=2)


