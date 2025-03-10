"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/10/21 21:23
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
3、js设置滚动条位置      
   driver.execute_script("document.documentElement.scrollTop=xx")
4、js的window.scrollTo()方法
    1、X轴：网页左上角，从左到右越来越大
    2、Y轴：网页左上角，从上到下越来越大
    3、window.scrollTo(0,0)：滑动到指定坐标位置
    4、window.scrollBy(0,0)：基于当前位置滑动指定像素距离
    5、document.body.scrollWidth：获取滚动条可滑动最大宽度
    6、document.body.scrollHeight：获取滚动条可滑动最大高度
    7、document.documentElement.scrollTop：获取当前滚动距离最上方的距离(垂直方向)
    8、document.documentElement.scrollLeft：获取当前滚动距离最左侧的距离(水平方向)
5、上下滚动
    driver.execute_script("window.scrollTo(x轴,y轴)")
    driver.execute_script("window.scrollTo(0,10000)")
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    driver.execute_script("document.documentElement.scrollTop=0")
6、左右滚动 
    x轴滑动100像素，y轴不变
    driver.execute_script("window.scrollTo(100,0)")
    driver.execute_script("document.documentElement.scrollLeft=100")
    driver.execute_script("window.scrollTo(0,document.body.scrollWidth)")                                    
7、其他操作
   1、执行js获取value属性值（text值获取不到的时候）【重点】
      attend_num = driver.execute_script('return arguments[0].value;',ele)
   2、js修改value属性值
      driver.execute_script("arguments[0].value=arguments[1]",ele1,value)  
   3、鼠标聚焦到element元素上
      driver.execute_script("arguments[0].focus();", element)


"""
import time
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
dr = webdriver.Chrome()
dr.get("https://www.baidu.com")
dr.implicitly_wait(5)
dr.find_element_by_xpath('//input[@id="kw"]').send_keys("柠檬班",Keys.ENTER)

time.sleep(3)
#通过js实现

# dr.execute_script("window.scrollTo(0,1000)")
# dr.execute_script("window.scrollTo(100,0)")

dr.execute_script("document.documentElement.scrollLeft=100")


