"""
============================
Project: py52Api
Author:柠檬班-海励
Time:2022/8/17 20:22
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
IP地址：47.113.180.81
账号：lemon
端口：3306
密码：lemon123
数据库：yami_shops

1、随机生成一个手机号，查询一次数据库看是否重复，如果存在了重新生成一个手机号再查询一次(while 循环)


"""

from api.mall.data import Data
import pymysql
import requests
from faker import Faker


class Register:
    def __init__(self):
        self.send_msg_url = "http://mall.lemonban.com:8107/user/sendRegisterSms"
        self.check_code_url = "http://mall.lemonban.com:8107/user/checkRegisterSms"
        self.register_url = "http://mall.lemonban.com:8107/user/registerOrBindUser"
        self.fk = Faker(locale="zh_cn")
        self.db = pymysql.connect(
            host="47.113.180.81",
            port=3306,
            user="lemon",
            password="lemon123",
            db="yami_shops",
            autocommit=True
        )
        self.cur = self.db.cursor()

    def __close_db(self):
        self.cur.close()
        self.db.close()

    #获取未注册的手机号
    def __get_phone_number(self):
        # 查询数据库看是否重复
        while True:
            phone = self.fk.phone_number()  # 去数据库去查询手机号是否重复，框架里面讲
            print(phone)
            sql = "select count(*) from tz_user where user_mobile='{}'".format(phone)
            # sql = "select count(*) from tz_user where user_mobile='17261557882'"
            self.cur.execute(sql)
            result = self.cur.fetchall()
            print("sql查询返回：", result, len(result))
            if result[0][0] > 0:
                # 已注册,重新生成手机号继续判断
                continue
            else:
                # 未注册
                setattr(self,"phone",phone)
                #设置全局属性，给登陆接口使用
                setattr(Data,"phone",phone)
                break

    # 发短信
    def __send_msg(self):
        #获取手机号
        # self.get_phone_number()
        data = {
            "mobile": getattr(self,"phone")
        }
        resp = requests.put(url=self.send_msg_url, json=data)
        print("发送短信：", resp.text)

    # 校验短信验证码
    def __check_msg_code(self):
        #发短信
        # self.send_msg()
        sql = f"select mobile_code from tz_sms_log where user_phone='{getattr(self,'phone')}' order by id desc limit 1"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        data = {
            "mobile": getattr(self,"phone"),
            "validCode": result[0][0]
        }
        resp = requests.put(url=self.check_code_url, json=data)
        print("校验短信验证码返回：",resp.text)
        setattr(self,"sms_flag",resp.text)

    # 注册
    def __register(self):
        #校验短信
        # self.check_msg_code()
        data = {
            "appType": 3,
            "checkRegisterSmsFlag": getattr(self,"sms_flag"),
            "mobile": getattr(self,"phone"),
            "userName": getattr(self,"phone"),
            "password": "123456",
            "registerOrBind": 1,
            "validateType": 1
        }
        resp = requests.put(url=self.register_url, json=data)
        print("注册接口返回：",resp.text)

    #注册流程
    def start(self):
        try:
            # 生成未注册的手机号
            self.__get_phone_number()
            # 发送短信
            self.__send_msg()
            # 校验短信验证码
            self.__check_msg_code()
            #注册
            self.__register()
        except Exception as e:
            pass
        finally:
            # 关闭数据库连接
            self.__close_db()

if __name__ == '__main__':
    cl = Register()
    cl.start()

