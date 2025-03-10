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
二、iframe切换
1、元素定位
//a[@id="switcher_plogin"]
//input[@id="u"]
//input[@id="p"]

2、切换iframe
   通过id或者name属性去切换
   dr.switch_to.frame('login_frame')
   
   通过元素定位的方式去找到元素，再切换进去
   eles = dr.find_elements_by_tag_name("iframe")
3、面试会被问到
   1、如何切换iframe
   2、xpath元素定位在浏览器上测试没有问题，到代码里面跑就报错找不到元素
   
4、切换到上一级页面
dr.switch_to.parent_frame()
    
5、切换到最外层页面
dr.switch_to.default_content()
"""

from selenium import webdriver
dr = webdriver.Chrome()
dr.get("https://mail.qq.com/")
dr.implicitly_wait(5)
#先切入iframe,通过name属性或者id属性,可以看源码
# dr.switch_to.frame('login_frame')
#通过元素定位方式(标签名称定位)
eles = dr.find_elements_by_tag_name("iframe")
print('eles>>>:',eles)
print(eles[1])
dr.switch_to.frame(eles[1])
dr.find_element_by_xpath('//a[@id="switcher_plogin"]').click()
dr.find_element_by_xpath('//input[@id="u"]').send_keys("627323423")

#切换到上一级页面
# dr.switch_to.parent_frame()

#切换到最外层页面
# dr.switch_to.default_content()

dr.find_element_by_xpath('//input[@id="p"]').send_keys("627323423")





