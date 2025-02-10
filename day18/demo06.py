"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/27 21:54
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、造测试数据
造的数据都是假的，人工智能生成的
http://testingpai.com/article/1615615023407
1、安装第三方库
pip install Faker==13.15.1

2、使用
本地化
fk = Faker(locale="zh-CN")

3、四要素(实名认证)
姓名
fk.name()

身份证
手机号
银行卡


"""

from faker import Faker

fk = Faker(locale="zh-CN")

print(fk.name())

print(fk.ssn())

print(fk.phone_number())














