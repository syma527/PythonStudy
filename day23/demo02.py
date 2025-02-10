"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/8/8 21:22
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、re正则表达式
单字符匹配
1、只能处理字符串类型的数据

2、. 匹配任意字符除换行符以外，每次匹配一个字符，返回list
test_str = "hello pythpon52"
ss = "h."
result = re.findall(ss,test_str)
print(result)

3、[] 匹配括号里面的任意一个字符
test_str = "hello pythpon52"
ss = "[hp]"
result = re.findall(ss,test_str)
print(result)

4、\d 匹配数字
test_str = "hello pythpon52"
ss = "\d"
result = re.findall(ss,test_str)
print(result)

5、\D匹配非数字
test_str = "hello pythpon52"
ss = "\D"
result = re.findall(ss,test_str)
print(result)

6、\S(大写)匹配非空白
test_str = "hello pythpon52"
ss = "\S"
result = re.findall(ss,test_str)
print(result)

7、\s(小写)匹配空格
test_str = "hello pythpon52"
ss = "\s"
result = re.findall(ss,test_str)
print(result)

8、\w(小写)匹配非特殊字符
test_str = "hello %^&*(%$#@!pythpon52"
ss = "\w"
result = re.findall(ss,test_str)
print(result)


9、匹配特殊字符(空格是特殊字符)
test_str = "hello %^&*(%$#@!pythpon52"
ss = "\W"
result = re.findall(ss,test_str)
print(result)


多字符匹配
1、* 匹配前一个字符出现0次或者无限次【贪婪模式】
test_str = "hello %^&*(%$#@!pythpyypopyyyyyn52"
ss = "py*" # p   py    pyy
result = re.findall(ss,test_str)
print(result)

2、+ 匹配前一个字符出现1次或者无限次，至少要匹配一个【贪婪模式】
test_str = "phello %^&*(%$#@!pythpyypopyyyyyn52"
ss = "py+" # p   py    pyy
result = re.findall(ss,test_str)
print(result)

3、?： 匹配前一个字符出现0次或者一次【非贪婪模式】
test_str = "phello %^&*(%$#@!pythpyypopyyyyyn52"
ss = "py?" # p   py    pyy
result = re.findall(ss,test_str)
print(result)

4、{n}匹配前一个字符出现n次
test_str = "phello %^&*(%$#@!pythpyypopyyyyyn52"
ss = "py{3}" # p   py    pyy
result = re.findall(ss,test_str)
print(result)

5、{m,n}匹配前一个字符出现m到n次
test_str = "phello %^&*(%$#@!pythpyyypopyyyyyn52"
ss = "py{3,5}" # p   py    pyy
result = re.findall(ss,test_str)
print(result)


6、逻辑或
test_str = "phello %^&*(%$#@!pythpyyypopyyyyyn52"
ss = "py|he|ll"
result = re.findall(ss,test_str)
print(result)
"""



import re


test_str = "phello %^&*(%$#@!pythpyyypopyyyyyn52"
ss = "py|he|ll"
result = re.findall(ss,test_str)
print(result)











