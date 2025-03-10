"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/10/21 20:41
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
十四、arguments对象        
1、什么是arguments   
	1、arguments 对象实际上是所在函数的一个内置类数组对象，arguments不是数组而是一个对象
	2、每个函数都有一个arguments属性，表示函数的实参集合 
2、arguments用法
	1、用于接收外部传进来的参数，固定写法   
	2、arguments[0]表示接收后面传入的第一个参数（与format类似，索引从0开始）
	3、可以写多个表达式,用分号隔开
		driver.execute_script("arguments[0].click();alert(arguments[1])", element,"弹框")

问题：如果遇到元素不能通过selenium的click来点击，解决方案有哪些
1、模拟鼠标操作
2、模拟键盘操作
3、通过js去操作


"""


from selenium.webdriver.common.keys import Keys

from selenium import webdriver
dr = webdriver.Chrome()
dr.get("https://www.ketangpai.com/#/login")
dr.implicitly_wait(5)
dr.find_element_by_xpath('//input[@placeholder="请输入邮箱/手机号/账号"]').send_keys("1605118090@qq.com")
dr.find_element_by_xpath('//input[@placeholder="请输入密码"]').send_keys("Aa123456")
ele = dr.find_element_by_xpath('//span[text()="登录"]/parent::button')
dr.execute_script("arguments[0].click();",ele)

