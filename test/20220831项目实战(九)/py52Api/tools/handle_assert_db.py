"""
============================
Project: py52Api
Author:柠檬班-海励
Time:2022/8/27 20:15
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
from tools.handle_mysql import mysql
from tools.handle_replace import HandleReplace

"""

数据库断言
"""
import json
from unittest import TestCase

class HandleAssertDb:
    def __init__(self):
        self.replace = HandleReplace()
        self.my_assert = TestCase()

    #数据库断言
    def assert_db(self,assert_db:str):
        try:
            if assert_db:
                #转换数据类型，将excel中的数据库断言数据转成dict
                assert_db = assert_db if isinstance(assert_db,dict) else json.loads(assert_db)
                #获取实际结果的sql语句
                sql = assert_db["actual_data"]
                #检查是否需要替换sql语句，如果需要就替换sql语句
                sql = self.replace.replace_sql(sql=sql)
                #执行sql语句
                result = mysql.get_data(sql=sql)
                #断言
                self.my_assert.assertEqual(assert_db["expected_data"],result[0])
                print("数据库断言成功")
            else:
                print("excel中assert_db字段为空，不需要断言")
        except Exception as e:
            print("assert_db执行报错了")



if __name__ == '__main__':

    cl = HandleAssertDb()
    db_data = """{"expected_data":1,"actual_data":"select count(*) from tz_attach_file where file_path = '#file_path#'"}"""

    cl.assert_db(assert_db=db_data)



