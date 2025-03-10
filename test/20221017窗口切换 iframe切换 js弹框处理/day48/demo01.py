"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/10/17 20:05
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、窗口切换
手动切换：
1、获取当前窗口句柄
	handle = driver.current_window_handle
2、获取所有窗口句柄(静态获取，如果新打开了窗口要重新获取一次) 
	handles = driver.window_handles
3、方式一切换窗口
	drive.switch_to.window(handles[-1])
	drive.switch_to.window(handles[0])
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
dr = webdriver.Chrome()
dr.get("https://www.baidu.com")
dr.maximize_window()
#隐式等待
dr.implicitly_wait(5)
#返回字符串
res = dr.current_window_handle
print("第一次获取的窗口句柄:",res)
# ['CDwindow-E5C6261258EA231A2852333FA613D2D9','CDwindow-E5C6261258EA231A2852333FA613D2D9']
dr.find_element_by_xpath('//input[@id="kw"]').send_keys("柠檬班")
dr.find_element_by_xpath('//input[@id="su"]').send_keys(Keys.ENTER)
dr.find_element_by_xpath('//a[contains(text(),"百度百科")]').click()
#动态获取窗口句柄
res2 = dr.window_handles
print("第二次获取的窗口句柄:",res2)
#切换到最新的窗口
dr.switch_to.window(window_name=res2[-1])
res3 = dr.current_window_handle
print("获取当前的窗口句柄:",res3)
dr.switch_to.window(window_name=res2[0])
time.sleep(3)
res4 = dr.current_window_handle
print("获取当前的窗口句柄:",res4)
time.sleep(5)

先判断再切换窗口：
new_window_is_opened类：
result = wait.until(EC.new_window_is_opened(res))


"""
from selenium.webdriver.common.by import By
#等待
from selenium.webdriver.support.wait import WebDriverWait
#等待条件
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
dr = webdriver.Chrome()
dr.get("https://www.baidu.com")
dr.maximize_window()
#显式等待
wait = WebDriverWait(driver=dr,timeout=5)
#返回字符串
res =dr.window_handles
print("第一次获取的窗口句柄:",res)
wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@id="kw"]'))).send_keys("柠檬班")
wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@id="su"]'))).send_keys(Keys.ENTER)
wait.until(EC.visibility_of_element_located((By.XPATH,'//a[contains(text(),"百度百科")]'))).click()
#动态获取窗口句柄
res2 = dr.window_handles
print("第二次获取的窗口句柄:",res2)
time.sleep(5)
#等待新窗口打开,判断是否真的新打开了窗口，返回布尔值,自己去判断为True再切换进去
result = wait.until(EC.new_window_is_opened(res))
if result:
    dr.switch_to.window(res2[-1])
res3 = dr.current_window_handle
print("获取当前的窗口句柄:",res3)
time.sleep(5)























