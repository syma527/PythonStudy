"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/8/10 19:59
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、re正则表达式
1、^: 匹配字符串开始位置
test_str = "hello python52"
ss = "^h"
result = re.findall(ss,test_str)
print(result)

2、$: 匹配字符串结尾位置
test_str = "hello python52"
ss = "n52$"
result = re.findall(ss,test_str)
print(result)

3、贪婪模式
贪婪模式(+)：至少匹配一次
test_str = "hello53454pyth65756on52"
ss = "\d+"
result = re.findall(ss,test_str)
print(result)
贪婪模式(*):会匹配出0次的数据
test_str = "hello53454pyth65756on52"
ss = "\d*"
result = re.findall(ss,test_str)
print(result)

4、非贪婪模式
test_str = "hello53454pyth65756on52"
ss = "\d+?"
result = re.findall(ss,test_str)
print(result)

5、分组匹配()
短信验证码提取：redis里面存的是短信验证码，无法连接redis
把验证码通过日志的方式打印出来，通过正则去提取验证码
jakdjflakdjf@1927@dfadfadfdfadf
test_str = "jakdjflakdjf@1927@dfadf5677adfdfadf"
ss = "@(\d.+)@"
result = re.findall(ss,test_str)
print(result)


"""
import re




# test_str = "jakdjflakdjf@1927@dfadf5677adfdfadf"
#字符串的匹配  找规律  设计正则查找的数据结构的规律
test_str = "jakdjf@lakdjf@1927dfadf5677adfdfadf"
ss = "@(\w.+)@"
result = re.findall(ss,test_str)
print(result)















