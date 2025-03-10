"""
============================
Project: py52Api
Author:柠檬班-海励
Time:2022/8/29 21:17
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""

"""

前置sql语句
ast.literal_eval()
eval()
不能有空格和换行符
"""



import json

from tools.handle_logs import my_log
from tools.handle_replace import HandleReplace
from tools.handle_mysql import mysql
from tools.handle_attribute import HandleAttr

class HandleSetupSql:

    def __init__(self):
        self.replace = HandleReplace()

    # [{"":""},{"":""}]
    #["select mobile_code from  tz_sms_log where  user_phone='#mobile#' order by id desc limit 1",""]
    def setup_sql(self,sql_list:str):
        try:
            my_log.info(msg="开始执行前置sql")
            my_log.info(msg=f"入参数据类型:{type(sql_list)}参数:{sql_list}")
            if sql_list:
                my_log.info(msg="sql_list不为空，需要执行前置sql语句")
                sql_list = sql_list if isinstance(sql_list,list) else json.loads(sql_list)
                for sql in sql_list:
                    #替换sql语句
                    sql = self.replace.replace_sql(sql=sql)
                    #执行sql语句
                    result = mysql.get_dict_data(sql=sql)
                    my_log.info(msg=f"前置sql执行结果{result}")
                    #设置为类属性
                    if len(result) > 0:
                        #遍历sql语句查询结果，有可能有多行数据，这里做了了兼容
                        for dict_data in  result:
                            #遍历list的没一个结果，一行数据
                            for key,value in dict_data.items():
                                my_log.info(msg=f"前置sql设置全局变量key={key},value={value}")
                                #设置属性
                                setattr(HandleAttr,key,value)
                    else:
                        my_log.info(msg="前置sql语句执行后返回结果为空，不需要设置属性")
            else:
                my_log.info(msg="sql_list为空，不需要执行前置sql去获取数据")
        except Exception as e:
            my_log.exception(msg=e)
            raise TypeError




if __name__ == '__main__':
    cl = HandleSetupSql()
    sql ="""["select mobile_code from  tz_sms_log where  user_phone='18820992515' order by id desc limit 1"]"""
    cl.setup_sql(sql)


