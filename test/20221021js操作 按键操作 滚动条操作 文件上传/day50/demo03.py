"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/10/21 20:26
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、按键操作

1、导入包
   from selenium.webdriver.common.keys import Keys
2、常用方法               
1、send_keys(Keys.BACK_SPACE)：删除键BackSpace,每次删除1个字符
2、send_keys(Keys.SPACE)：空格键Space
3、send_keys(Keys.TAB)：制表键Tab
4、send_keys(Keys.ESPACE)：回退键Esc
5、send_keys(Keys.ENTER)：回车键Enter
6、send_keys(Keys.CONTROL,‘a’)：全选Ctrl+A
7、send_keys(Keys.CONTROL,‘c’)：复制CTRL+C
8、send_keys(Keys.CONTROL,‘x’)：剪切CTRL+X
9、send_keys(Keys.CONTROL,‘v’)：粘贴Ctrl+V
10、send_keys(Keys.F1)：键盘F1
11、send_keys(Keys.F12)：键盘F12



"""
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
dr = webdriver.Chrome()
dr.get("https://www.baidu.com")
dr.implicitly_wait(5)
dr.find_element_by_xpath('//input[@id="kw"]').send_keys("柠檬班",Keys.ENTER)










