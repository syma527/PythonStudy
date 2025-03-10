"""
============================
Project: py52Api
Author:柠檬班-海励
Time:2022/8/24 20:20
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""

import json
from jsonpath import jsonpath
from unittest import TestCase



class HandleResponse:
    def __init__(self):
        self.my_assert = TestCase()

    #响应结果处理
    def handle_response(self,response):
        #1、有参数接收响应结果   2、根据数据类型判断是否需要二次封装
        try:
            if isinstance(response.json(),dict):
                #返回response.json()
                return {"response":response.json()}
        except Exception as e:
            #执行报错了，response.text  二次封装成json
            return  {"response":response.text}

    #接口断言
    def assert_responsee(self,response,expected_data):
        """
        #期望结果==我们实现设置好的结果 {"token_type":"bearer"}
        #实际结果==接口执行返回的结果
        1、从excel读取期望结果的值
        2、遍历期望结果的key,通过key从响应结果中提取对应的value
        3、断言期望和实际结果
        :param response:
        :param expected_data:
        :return:
        """
        if expected_data:
            # 创建空字典，存放实际结果
            actual_data = {}  # {"token_type":"bearer"}
            # 将期望结果转换成python对象
            expected_data = expected_data if isinstance(expected_data,dict) else json.loads(expected_data)
            for key in expected_data:
                #从响应结果中获取key对应的value,取出来的是list  # ["bearer"]
                actual_data[key] = jsonpath(response, f"$..{key}")[0]
            #断言期望结果和实际结果
            self.my_assert.assertEqual(expected_data,actual_data)
        else:
            print("exlcel中expected_data为空，该接口响应结果不需要断言")
