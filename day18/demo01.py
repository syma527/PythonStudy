"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/27 20:12
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


test_dict = {
"section1":{"option1":"val","option2":"val"},
"section2":{"option1":"val","option2":"val"},
}


2、获取str类型
get_str = conf.get(section="mysql", option="host")
print(get_str,type(get_str))

3、获取int类型
get_int = conf.getint(section="mysql", option="passwd")
print(get_int,type(get_int))

4、获取小数
get_float = conf.getfloat(section="mysql", option="float")
print(get_float,type(get_float))

5、获取布尔值
get_bool = conf.getboolean(section="mysql", option="is_file")
print(get_bool,type(get_bool))

二、添加操作【了解】
1、添加是往内存里面加，不是往实际文件里面写数据
添加section
conf.add_section("py52")
添加option
conf.set(section="py52",option="key1",value="旧梦")
删除
conf.remove_option(section="py52",option="key1")
将内存中添加的数据写到文件里面去
with open(file="test.ini",mode="w") as file:
    conf.write(fp=file)


"""
from configparser import ConfigParser
conf = ConfigParser()
#读到内存里面去
conf.read(filenames="test.ini",encoding="utf-8")

res1 = conf.sections()
print(res1)

#添加是往内存里面加，不是往实际文件里面写数据
#往内存中加section
conf.add_section("py52")

res2 = conf.sections()
print(res2)

#往内存中添加option
conf.set(section="py52",option="key1",value="旧梦")


conf.remove_option(section="py52",option="key1")

res3 = conf.get(section="py52",option="key1")
print(res3)

#将内存中添加的数据写到文件里面去
with open(file="test.ini",mode="w") as file:
    conf.write(fp=file)

"""
from configparser import ConfigParser
conf = ConfigParser()
#读到内存里面去
conf.read(filenames="test.ini",encoding="utf-8")


#获取section
# conf.sections()
#获取option
# conf.options(section="mysql")

#获取指定section下的option值
#获取str类型
get_str = conf.get(section="mysql", option="host")
print(get_str,type(get_str))
#获取int类型
get_int = conf.getint(section="mysql", option="passwd")
print(get_int,type(get_int))
#获取小数
get_float = conf.getfloat(section="mysql", option="float")
print(get_float,type(get_float))
#获取布尔值
get_bool = conf.getboolean(section="mysql", option="is_file")
print(get_bool,type(get_bool))
"""








