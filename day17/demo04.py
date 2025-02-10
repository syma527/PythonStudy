"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/25 21:39
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
配置文件
一、ini配置文件【不用】
{
"section1":{"option1":"val","option2":"val"},
"section2":{"option1":"val","option2":"val"},
}

django里面用setting.py文件做配置文件

1、获取所有的section,返回section名称的list
res = conf.sections() #获取到的是具体的值
res = conf.keys() #获取到的是对象

二、yaml【不用】


三、py文件【使用】

"""

test_dict = {
"section1":{"option1":"val","option2":"val"},
"section2":{"option1":"val","option2":"val"},
}

from configparser import ConfigParser

conf = ConfigParser()

conf.read(filenames="test.ini",encoding="utf-8")

#获取所有section
# res = conf.sections()
# res = conf.keys()

# print(res)
# for i in res:
#     print(i)


#获取指定section里面所有的option
res = conf.options(section="mysql")
print(res)


res2 = conf.items(section="mysql")
print(res2)



from day17.setting import test_dict


