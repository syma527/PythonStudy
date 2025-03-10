"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/10/14 21:28
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""


"""
三、元素等待
1、强制等待(秒)
import time
time.sleep(1)

2、隐式等待(秒)
dr.implicitly_wait(5)
整个会话只需要执行一次,全局起作用,在5秒内反复去找该元素,如果找到了就往下执行代码,如果没找到就报错了

3、显式等待(智能等待)
1、某个时间内,设置一个等待操作条件(一直去找某个元素)，设置间隔时间

第一种写法：
wait = WebDriverWait(driver=dr,timeout=10,poll_frequency=1)
ele1 = wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@placeholder="用户名"]')))

第二种写法：
#第二种写法
loc_path = (By.XPATH,'//input[@placeholder="用户名"]')
element = WebDriverWait(driver=dr,timeout=10,poll_frequency=1).until(EC.visibility_of_element_located(loc_path))


四、expected_conditions类条件方法
	a、常用
	1、visibility_of_element_located
       判断某个元素是否可见. 可见代表元素非隐藏，并且元素的宽和高都不等于0
	2、visibility_of_all_elements_located
	  判断多个元素是否可见,传入定位表达式,可见代表元素非隐藏，并且元素的宽和高都不等于0
	3、visibility_of 
       作用同visibility_of_all_elements_located传定位到的element,非定位表达式locator                
	4、frame_to_be_available_and_switch_to_it
       判断该frame是否可以switch进去，如果可以的话，返回True并且switch进去，否则返回False
	5、alert_is_present
       判断页面上是否存在alert
	6、element_to_be_selected
        判断某个元素是否被选中了,一般用在下拉列表
	7、element_to_be_clickable
        判断某个元素中是否可见并且是enable的，这样的话才叫clickable
	8、presence_of_element_located
        判断某个元素是否被加到了dom树里，【并不代表该元素一定可见】
	9、presence_of_all_elements_located
        等待所有元素存在dom树中【并不代表该元素一定可见】
    
	b、不常用
	1、title_is
        判断当前页面的title是否完全等于（==）预期字符串，返回布尔值
	2、title_contains
        判断当前页面的title是否包含预期字符串，返回布尔值
	3、text_to_be_present_in_element
        判断某个元素中的text是否包含了预期的字符串
	4、text_to_be_present_in_element_value
        判断某个元素中的value属性是否包含了预期的字符串
	5、invisibility_of_element_located
        判断某个元素中是否不存在于dom树或不可见
	6、staleness_of
        等某个元素从dom树中移除，返回布尔值
	7、element_selection_state_to_be
       判断某个元素的选中状态是否符合预期
	8、element_located_selection_state_to_be
       作用同element_selection_state_to_be传定位到的element,非定位表达式locator      
"""

import time

from selenium import webdriver

from selenium.webdriver.common.by import By
#等待
from selenium.webdriver.support.wait import WebDriverWait
#等待条件
from selenium.webdriver.support import expected_conditions as EC

dr = webdriver.Chrome()
dr.get(url="http://mall.lemonban.com/admin/#/login")
#隐式等待
# dr.implicitly_wait(5)


#显式等待
wait = WebDriverWait(driver=dr,timeout=10,poll_frequency=1)
ele1 = wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@placeholder="用户名"]')))
ele1.send_keys("student")

ele2 = wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@placeholder="密码"]')))
ele2.send_keys("123456a")

ele3 = wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@placeholder="验证码"]')))
ele3.send_keys("lemon")

ele4 = wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@value="登录"]')))
ele4.click()

time.sleep(10)
dr.close()



