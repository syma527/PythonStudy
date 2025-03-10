"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/10/14 19:55
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、轴定位
1、轴定位之父节点parent
语法：
//div[text()=" 课程教学 "]/parent::div
//div[text()=" 课程教学 "]/parent::div/parent::div
注意: 轴后面写什么标签就找什么标签

2、轴定位之祖先节点ancestor(包括父节点)
语法:
//div[text()=" 课程教学 "]/ancestor::div
//div[text()=" 课程教学 "]/ancestor::div[@id="viewClassDetailRoot"]

3、轴定位之当前节点【之后】的所有节点following
所有兄弟节点，会递归找
语法：
//div[@id="viewClassDetailRoot"]/following::div
//div[@id="viewClassDetailRoot"]/following::div/parent::div

4、轴定位之当前节点【之前】的所有节点preceding
语法:
//div[@id="viewClassDetailRoot"]/preceding::div

5、轴定位之当前节点【之后】的所有兄弟节点following-sibling
所有兄弟节点，不会递归找
语法:
//div[@id="viewClassDetailRoot"]/following-sibling::div

6、轴定位之当前节点【之前】的所有兄弟节点preceding-sibling
语法:
//div[@id="viewClassDetailRoot"]/preceding-sibling::div
//div[@id="viewClassDetailRoot"]/preceding-sibling::div[@class="global-loading-box"]

"""