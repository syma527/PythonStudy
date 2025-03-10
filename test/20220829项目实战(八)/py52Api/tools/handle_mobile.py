"""
============================
Project: py52Api
Author:柠檬班-海励
Time:2022/8/29 20:35
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
from faker import Faker

from tools.handle_mysql import mysql


class HandleMobile:
    def __init__(self):
        self.fk = Faker(locale="zh_cn")

    #获取未注册的手机号
    def get_phone_number(self):
        # 查询数据库看是否重复
        while True:
            phone = self.fk.phone_number()  # 去数据库去查询手机号是否重复，框架里面讲
            print(phone)
            sql = "select count(*) from tz_user where user_mobile='{}'".format(phone)
            result = mysql.get_data(sql=sql)
            if result[0] > 0:
                # 已注册,重新生成手机号继续判断
                continue
            else:
                # 未注册
                return phone

if __name__ == '__main__':
    cl = HandleMobile()
    cl.get_phone_number()