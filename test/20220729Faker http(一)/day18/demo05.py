"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/27 21:43
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
单例模式



"""


import pymysql
from day18.setting import mysql_info


class Mysql:
    def __init__(self):
        #创建连接
        self.db = pymysql.connect(
                    host=mysql_info["host"],
                    port=mysql_info["port"],
                    user=mysql_info["user"],
                    password=mysql_info["password"],
                    charset=mysql_info["charset"],
                    autocommit=mysql_info["autocommit"], #自动提交修改
                    db=mysql_info["db"],
                    cursorclass=pymysql.cursors.DictCursor #设置返回数据的类型为字典
                )
        self.cur = self.db.cursor() #创建游标

    def get_datas(self,sql):
        try:
            self.cur.execute(sql)
            return self.cur.fetchall()
        except Exception as e:
            print("执行报错了")
        finally:
            self.db_close()

    def db_close(self):
        self.cur.close()
        self.db.close()

if __name__ == '__main__':
    sql = "SELECT * FROM  tz_attach_file  WHERE file_id < 20"
    cl = Mysql()
    result = cl.get_datas(sql)
    print(result)