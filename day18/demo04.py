"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/27 20:58
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

一、mysql操作
1、安装pymysql
pip install PyMySQL==1.0.2

2、使用
执行sql语句
cur.execute(sql)

返回查询到的所有结果
res1 = cur.fetchall()

返回查询到的第一个结果
res2 = cur.fetchone()

查询返回的结果数可以通过size指定，默认返回第一个查询结果
res3 = cur.fetchmany(size=3)

"""
import pymysql
from day18.setting import mysql_info
db = pymysql.connect(
                    host=mysql_info["host"],
                    port=mysql_info["port"],
                    user=mysql_info["user"],
                    password=mysql_info["password"],
                    charset=mysql_info["charset"],
                    autocommit=mysql_info["autocommit"], #自动提交修改
                    db=mysql_info["db"],
                    cursorclass=pymysql.cursors.DictCursor #设置返回数据的类型为字典
                )
#sql执行的窗口
cur = db.cursor()
sql = "SELECT * FROM  tz_attach_file  WHERE file_id < 20"
#执行sql语句
cur.execute(sql)
#返回查询到的所有结果
# res1 = cur.fetchall()
#返回查询到的第一个结果
# res2 = cur.fetchone()
#查询返回的结果数可以通过size指定，默认返回第一个查询结果
res3 = cur.fetchmany(size=3)
print(len(res3),res3)
cur.close()
db.close()


#with语法实现
with pymysql.connect(
                    host=mysql_info["host"],
                    port=mysql_info["port"],
                    user=mysql_info["user"],
                    password=mysql_info["password"],
                    charset=mysql_info["charset"],
                    autocommit=mysql_info["autocommit"], #自动提交修改
                    db=mysql_info["db"],
                    cursorclass=pymysql.cursors.DictCursor #设置返回数据的类型为字典

                ) as db:
    cur = db.cursor()
    cur.execute("sql")
    cur.fetchall()