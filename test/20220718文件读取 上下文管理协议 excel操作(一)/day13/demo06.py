"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/15 21:40
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
路径处理
1、获取当前执行文件的绝对路径
print(__file__)

2、获取当前执行文件所在目录的绝对路径
my_path = os.path.dirname(__file__)

3、获取指定文件的绝对路径
没有传路径的时候，默认是当前路径下
res = os.path.abspath("demo01.py")

4、路径拼接
res = os.path.abspath(__file__)
print(res)

my_path = os.path.dirname(res)
print(my_path)

result = os.path.dirname(my_path)
print(result)

# D:\vip_class\py52   , "day02" , "demo03.py"
new_path = os.path.join(result,"day02","demo03.py")
print(new_path)

"""

import os

# print(__file__)
# my_path = os.path.dirname(__file__)
# print(my_path)
# res = os.path.abspath("demo01.py")
# print(res)



#相对路径\   /
# res = os.path.join(r"vip_class","py52","index.html")
# print(res)

#日志文件   配置文件   测试数据文件   图片上传

res = os.path.abspath(__file__)
print(res)

my_path = os.path.dirname(res)
print(my_path)

result = os.path.dirname(my_path)
print(result)
# D:\vip_class\py52   , "day02" , "demo03.py"
new_path = os.path.join(result,"day02","demo03.py")
print(new_path)
