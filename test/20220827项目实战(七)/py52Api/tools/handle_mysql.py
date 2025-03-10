"""
============================
Project: py52Api
Author:柠檬班-海励
Time:2022/8/27 20:04
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
"""


import pymysql
from conf.setting import mysql_info

class HandleMysql:
    def __init__(self):

        self.db = pymysql.connect(
                        host=mysql_info["host"],
                        port=mysql_info["port"],
                        user=mysql_info["user"],
                        password=mysql_info["password"],
                        db=mysql_info["db"],
                        autocommit=True,
                        charset="utf8"
                        )

        self.cur = self.db.cursor()

    #关闭数据库连接
    def close_db(self):
        self.cur.close()
        self.db.close()

    #查询数据，返回元组
    def get_data(self,sql):
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result


#单例
mysql = HandleMysql()
