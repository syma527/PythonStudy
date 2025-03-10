"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/10/14 20:43
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
二、元素操作
1、点击
element.click()
2、赋值
element.send_keys("student")
3、清空输入框
element.clear()
4、获取标签名称
res1 = ele2.tag_name
5、获取input输入的值
res2 = ele2.get_attribute('value')
res2 = ele3.text

二、浏览器操作
1、窗口最大化
driver.maximize_window()
2、窗口最小化
driver.minimize_window()
3、刷新
driver.refresh()
4、前进
driver.forward()
5、后退
driver.back()
6、关闭页签
driver.close()
7、退出浏览器
driver.quit()
8、获取cookies
driver.get_cookies()
9、添加cookies
driver.add_cookie(cookie_dict)
10、获取当前句柄
driver.window_handles
['CDwindow-AA2000884E0049C32EA2F5A536A03A7C','']
11、获取当前url地址
driver.current_url
12、截图保存
driver.get_screenshot_as_file(r"D:\20221014.png")


"""

import time

from selenium import webdriver

dr = webdriver.Chrome()
dr.get(url="http://mall.lemonban.com/admin/#/login")

time.sleep(2)
ele1 = dr.find_element_by_xpath('//input[@placeholder="用户名"]')
ele1.send_keys("student")

ele2 = dr.find_element_by_xpath('//input[@placeholder="密码"]')
ele2.send_keys("123456a")

ele3 = dr.find_element_by_xpath('//input[@placeholder="验证码"]')
ele3.send_keys("lemon")

# 清空
# ele1.clear()


# 获取标签名称
# res1 = ele2.tag_name
# print(res1)

# 获取Input输入的值
# res2 = ele2.get_attribute('value')
# res2 = ele3.text
# print(res2)

ele4 = dr.find_element_by_xpath('//input[@value="登录"]')
ele4.click()

time.sleep(5)

# url = dr.current_url
# print(url)

# 后退
# dr.back()

# time.sleep(5)
# 前进
# dr.forward()
res3 = dr.window_handles
print(res3)

dr.get_screenshot_as_file(r"D:\20221014.png")

time.sleep(5)

# dr.current_window_handle

dr.close()
