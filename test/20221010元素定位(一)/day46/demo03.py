"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/10/10 21:17
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、xpath定位
1、xpath定位特点
	1、万能定位方式
	2、支持文本内容进行定位
	3、支持根据元素的多个属性进行定位
	4、支持通过元素层级关系定位

2、xpath定位分类
	1、绝对路径定位
        1、体现父子关系、兄弟关系
		2、过于依赖当前页面元素结构，不稳定
	2、相对路径定位
		1、不考虑位置，不考虑层级
		2、在整个html页面找，只要表达式能匹配到就可以 

二、xpath定位方法
1、标签名称
语法：//标签名称
案例：//input
注意：不单独使用

2、标签名称+属性
语法：//标签名称[@属性名称="属性的值"]
案例：
单个属性
//input[@class="s_ipt"]

3、逻辑运算
多个属性通过and做逻辑运算(同时满足)
//input[@class="s_ipt" and @name="wd"]
多个属性通过or做逻辑运算(满足任意一个)
//input[@class="s_ipt" or @name="wd"]

4、文本定位(精准匹配)
语法：//标签名称[text()="文本内容"]
案例：
//a[text()="新闻"]
//a[text()="地图" and @class="mnav c-font-normal c-color-t"]

5、文本定位(包含某个文本内容)
语法://标签名称[contains(text(),"包含内容")]
    //标签名称[contains(@属性名称,"包含内容")]
案例：
//a[contains(text(),"新")]
//a[contains(text(),"新") and @class="mnav c-font-normal c-color-t"]


三、轴定位
定义、同过元素的相对位置来定位，相对的位置就叫轴


语法：已知元素/轴名称::标签名称[@属性名称="属性值" and @属性名称="属性值""]
      //轴：在当前节点下所有子孙节点去找元素
      /轴：在当前之后的所有节点去找元素(递归所有兄弟节点)

1、轴定位之父节点parent
语法：
//div[text()=" 课程教学 "]/parent::div
//div[text()=" 课程教学 "]/parent::div/parent::div


2、轴定位之祖先节点ancestor(包括父节点)




"""
import time
from selenium import webdriver

dr = webdriver.Chrome(r'D:\chromeDriver\105\chromedriver.exe')
dr.get(url="https://www.baidu.com/")
time.sleep(1)
ele = dr.find_element_by_xpath('//input[@class="s_ipt" and @name="wd"]')
ele.send_keys('py52')
time.sleep(10)
dr.quit()


