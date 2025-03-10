"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/6/24 20:13
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、字符串的转义【掌握】
1、取消转义：\ 让有特殊含义的字符按照字符串的样子输出，不执行特殊含义
2、取消转义：r 让有特殊含义的字符按照字符串的样子输出，不执行特殊含义

二、字符串的常用方法
单词大小写相关【掌握】
1、将所有字母转成大写
result = result.upper()
2、将所有字母转成小写
result = result.lower()
3、大小写互换
test_str = test_str.swapcase()
4、每个单词的首字母大写
test_str = test_str.title()

统计相关
1、统计字符串的长度(空格也占一个索引位置，有多少个空格就占多少个索引位)【掌握】
res = len(test_str)
2、统计某个元素出现的次数
可以通过索引值指定统计范围
res = test_str.count("h",2,len(test_str))

判断相关【返回布尔值】
1、判断字符串是否都是大写组成【掌握】
res = test_str.isupper()
2、判断字符串是否都是小写组成【掌握】
res = test_str.islower()
3、判断是否都是空格
res = test_str.isspace()
4、以某某开头【掌握】
res = test_str.startswith("http")
5、以某某结尾【掌握】
res = test_str.endswith(".html")
6、字符串是否都是数字【掌握】
res = test_str.isdigit()

字符串拆分【掌握】
1、第一个参数是拆分字符，拆分字符在拆分过程中会被丢弃掉
2、第二个参数是拆分的次数，可以自定义，默认是-1，表示不限制拆分次数
3、返回的是一个list
res = test_str.split(".",1)

字符串连接
1、字符串拼接【掌握】
test_str1 = "hello"
test_str2 = "python"
res = test_str1+test_str2
2、字符串连接【掌握】
res = '_'.join(test_str1)

字符串的替换【掌握】
1、第一个参数需要替换谁
2、第二个参数拿什么来替换
3、替换次数，不传，默认全部替换
test_str = "www.lemon.com"
res = test_str.replace("w","M")
res = test_str.replace("w","M",2)

res = test_str.strip("m")
移除字符串首尾的字符，默认移除的是换行符和空格
如果指定了移除字符，空格和换行符就不会被移除了

"""
test_str = " www.lemon.com"
res = test_str.replace("m","")
print(res)


# res = test_str.replace("w","M")
# print(res)

#移除字符串首尾的字符，默认移除的是换行符和空格
#如果指定了移除字符，空格和换行符就不会被移除了
# print("移除之前：",len(test_str))
# res = test_str.strip("m")
# print("移除之后：",len(res))
# print(res)



#python实现的是轮子和部件，你要造什么车子，你自己去找零件自己组装







"""

test_str1 = "hello"
h-e-l-l-o
res = '_'.join(test_str1)
print(res)

wwwlemoncom
test_str = "www.lemon.com"
res = test_str.split(".")
print(res)
res = '.'.join(res)
print(res)



test_str1 = "hello"
test_str2 = "python"
res = test_str1+test_str2
print(res)


test_str = "www.lemon.com"
res = test_str.split(".",1)
print(res)


test_str = "12300"
res = test_str.isdigit()
print(res)


num = input("用户输入：")
print(type(num))




test_str = "http://www.lemon.com/api/login"

# res = test_str.startswith("http")
#测试报告，历史测试报告.html，保留历史报告，展示最新的测试报告
res = test_str.endswith(".html")
print(res)


test_str = " "
res = test_str.isspace()
print(res)


test_str = "python"
res = test_str.isupper()
print(res)

res = test_str.islower()
print(res)


test_str = "hello python"
res = test_str.count("h",2,len(test_str))
print(res)




#统计字符串的长度
res = len(test_str)
print(res)




test_str = "hello python"
test_str = test_str.title()
print(test_str)




test_str = "hello PYTHON"
test_str = test_str.swapcase()
print(test_str)


result = input("输入验证码：")
print(id(result))
result = result.upper()
print(id(result))
result = result.lower()
print(id(result))


print("hello \\n python")
print(r"hello \n python")
dir_path = r"D:\test.py"  # \name_list.py
print(dir_path)

"""

test_str = " www.lemon.com"
res = test_str.replace("m","")
print(res)

