"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/27 20:34
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
二、yaml【不用】
1、语法：
写字典：
key1: val1
key2: val2
key3: val3



test.yaml = {"key1":"val1","key2":"val2","key3":"val3"}


2、使用
安装第三方包
pip install PyYAML==5.3.1

3、特点
   1、只能一次性读取数据出来，读取的是python对象
   2、支持的数据类型，整个yaml文件对外只有一个数据类型（dict  + list  + 纯量数据）
   3、支持嵌套，字典嵌套列表
   4、:表示字典，-：表示列表，符号后面一定要加空格
   5、用#表示注释
   6、大小写敏感
字典
key1: val1
key2: val2
key3: val3

字典嵌套列表
key1: val1
key2: val2
key3:
  - val1
  - val3
  - val2




"""


import yaml

# file = open(file="test.yaml",encoding="utf-8")
# #加载文件中的数据到内存中
# value = yaml.load(stream=file,Loader=yaml.FullLoader)
# print(value,type(value))
# file.close()

#with语法
with open(file="test.yaml",encoding="utf-8") as file:
    value = yaml.load(stream=file, Loader=yaml.FullLoader)
    print(value, type(value))









