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


from tools.handle_attribute import HandleAttr

class HandleReplace:
    def replace_data(self,data:str):
        """
        1、获取需要替换的数据
        2、遍历需要替换的数据，根据对应的数据生成对应的值
        :return:
        """
        if data:
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
                #替换数据
                for key in key_list:
                    data = data.replace(f"#{key}#",getattr(HandleAttr,key))
                data = json.loads(data)
                return data
            else:
                print("不需要替换请求参数，直接返回json数据")
                data = json.loads(data)
                return data
        else:
            print("请求参数为空，不需要替换参数")
            return {}


if __name__ == '__main__':
    cl = HandleReplace()

    data = str({
 "t": "#time#",
 "principal": "student",
 "credentials": "123456a",
 "sessionUUID": "#sessionUUID#",
 "imageCode": "lemon"

})
    cl.replace_data(data)

