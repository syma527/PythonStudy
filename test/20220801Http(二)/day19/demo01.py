"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/29 19:26
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
fk.ssn()
手机号
fk.phone_number()
银行卡
fk.credit_card_number()

4、个人信息
邮箱
email = fk.email()
工作
job = fk.job()
地址
addr = fk.address()
公司名称
comp = fk.company()
城市
city = fk.city()


5、随机数
fk.random_int(100, 500)
fk.word()


6、时间
过去的时间
年
fk.year()
当前年份的年月日
res = fk.date_this_year()
当前年份当前月的随机一天
res1 = fk.date_this_month()
年月日1970-现在
fk.date()
年月日时分秒
res2 = fk.date_time()

指定时间范围(年-月-日)
res = fk.date_between(start_date="-2y",end_date="today")
-1y: 一年前
-1m: 一个月前
today: 今天

指定时间范围(年-月-日 时:分:秒)
res2 = fk.date_time_between(start_date="-2y",end_date="now")
-1y: 一年前
-1m: 一个月前
now: 现在时刻

时间戳
fk.unix_time()

未来时间
年月日
future = fk.future_date()
年月日 时分秒
fur = fk.future_datetime()


7、数据不重复
res = [ fk.unique.name() for i in range(10)]





"""

from faker import Faker
fk = Faker(locale="zh-CN")

#造交易订单 对账(对平、挂账、销账)
future = fk.future_date()
print(future)
fur = fk.future_datetime()
print(fur)
res = [ fk.unique.name() for i in range(10)]
print(res)
test_list = []
for i in range(10):
    test_list.append(fk.unique.name())
print(test_list)

"""


#year   month   2020-7-29   2021-7-29
res = fk.date_between(start_date="-2y",end_date="today")


res2 = fk.date_time_between(start_date="-2y",end_date="now")
print(res2)
import time
print(time.time())
# time.strftime("%Y%m%d %H%M%S",time.time())
print(fk.unix_time())




print(fk.year())

print(fk.month())

res = fk.date_this_year()
print(res)

res1 = fk.date_this_month()
print(res1)

#1970 -  现在
print(fk.date())

res2 = fk.date_time()
print(res2)




# print(fk.name())
# print(fk.ssn())
# print(fk.phone_number())
# caer_no = fk.credit_card_number()
# print(caer_no)

addr = fk.address()
print(addr)
post_code = fk.postcode()
print(post_code)
email = fk.email()
print(email)
job = fk.job()
print(job)
comp = fk.company()
print(comp)
city = fk.city()
print(city)
import random
print(random.randint(100,500))
print(fk.random_int(100, 500))
print(fk.word())

"""