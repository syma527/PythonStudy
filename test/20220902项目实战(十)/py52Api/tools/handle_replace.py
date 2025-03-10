"""
============================
Project: py52Api
Author:柠檬班-海励
Time:2022/8/19 21:19
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""


"""
{
 "t": "#time#",
 "principal": "student",
 "credentials": "123456a",
 "sessionUUID": "#sessionUUID#",
 "imageCode": "lemon"

}

"""
import re
import time
import uuid
import json

from tools.handle_logs import my_log
from tools.handle_attribute import HandleAttr
from tools.handle_mobile import HandleMobile

class HandleReplace:

    def __init__(self):
        self.mobile = HandleMobile()

    #替换请求数据
    def replace_data(self,data:str):
        """
        1、获取需要替换的数据
        2、遍历需要替换的数据，根据对应的数据生成对应的值
        :return:
        """
        my_log.info(msg="开始执行请求参数替换")
        my_log.info(msg=f"入参数据类型:{type(data)},入参:{data}")
        if data:
            # ["time","time","file_path","file_path"]  ["mobile"]
            key_list = re.findall("#(\w.+?)#",data)
            print(key_list)
            if len(key_list) > 0:
                #生成需要替换的数据
                for key in key_list:
                    if key == "time":
                        times = str(int(time.time() * 1000))
                        setattr(HandleAttr,key,times)
                    elif key == "sessionUUID":
                        session_uuid = str(uuid.uuid4())
                        setattr(HandleAttr,key,session_uuid)
                    #产品编码不能重复
                    elif key == "party_code":
                        if not hasattr(HandleAttr,key):
                            code = str(int(time.time() * 1000))
                            setattr(HandleAttr, key, code)
                        else:
                            my_log.info(msg="产品编码已存在，不需要重复生成")
                    #处理手机号，需要查询数据库返回未注册的手机号，设置为属性
                    elif key == "mobile":
                        if not hasattr(HandleAttr,key):
                            mobile = self.mobile.get_phone_number()
                            setattr(HandleAttr, key, mobile)
                        else:
                            my_log.info(msg="mobile已存在，不需要重新生成未注册的手机号")

                #替换数据
                for key in key_list:
                    data = data.replace(f"#{key}#",str(getattr(HandleAttr,key)))
                data = json.loads(data)
                my_log.info(msg=f"替换请求参数后，返回json数据：{data}")
                return data
            else:
                data = json.loads(data)
                my_log.info(msg=f"不需要替换请求参数，直接返回json数据：{data}")
                return data
        else:
            my_log.info(msg="请求参数为空，不需要替换参数")
            return {}

    # 替换sql语句
    # select *from tz_attach_file where file_path = "2022/08/e52b0de43ce142c7844d2f83435062de.png";
    def replace_sql(self,sql:str):
        my_log.info(msg="开始执行sql语句替换方法replace_sql")
        # setattr(HandleAttr,"file_path","2022/08/e52b0de43ce142c7844d2f83435062de.png")
        if sql:
            key_list = re.findall("#(\w.+?)#", sql)
            if len(key_list) > 0:
                my_log.info(msg="sql语句需要进行参数替换")
                #获取sql替换需要的数据，这里默认从全局变量获取，暂时不做拓展
                #替换sql语句
                for key in key_list:
                    my_log.info(msg=f"替换之前sql:{sql}")
                    sql = sql.replace(f"#{key}#",getattr(HandleAttr,key))
                my_log.info(msg=f"替换之后sql:{sql}")
            else:
                my_log.info(msg="sql语句不需要替换数据")
        else:
            my_log.info(msg="sql语句为空，不需要替换")
        my_log.info(msg=f"返回的sql:{sql}")
        return sql



if __name__ == '__main__':
    cl = HandleReplace()

    data = str({
 "t": "#time#",
 "principal": "student",
 "credentials": "123456a",
 "sessionUUID": "#sessionUUID#",
 "imageCode": "lemon"

})


    sql = "select *from tz_attach_file where file_path =1111"
    cl.replace_sql(sql)
