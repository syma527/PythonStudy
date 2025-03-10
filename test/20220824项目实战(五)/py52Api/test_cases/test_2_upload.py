"""
============================
Project: py52Api
Author:柠檬班-海励
Time:2022/8/24 21:32
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""



"""

import requests
import unittest
from ddt import data, ddt

from tools.handle_excel import HandleExcel
from tools.handle_path import case_data_dir

from tools.handle_replace import HandleReplace
from tools.handle_response import HandleResponse
from tools.handle_extract_data import HandleExtractData
from tools.handle_request import HandleRequest

# 从excel中拿到login页的测试数据
case_list = HandleExcel(file_name=case_data_dir, sheet_name="login").get_cases()


@ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.header = {"locale": "zh_CN"}
        cls.replace = HandleReplace()
        cls.response = HandleResponse()
        cls.extract = HandleExtractData()
        cls.request = HandleRequest()

    @data(*case_list)
    def test_login(self, case):
        # 替换请求参数
        data = self.replace.replace_data(data=case["data"])
        print("请求参数的数据类型:", type(data))
        #发请求
        self.request.send_request()
        # resp = requests.request(method=case["method"], url=case["url"], json=data, headers=self.header)
        # print('响应结果：', resp.text)
        #响应结果处理
        new_response = self.response.handle_response(response=resp)
        #接口断言
        self.response.assert_responsee(response=new_response, expected_data=case["expected_data"])
        #提取数据，设置为类属性
        self.extract.extract_data(response=new_response,extract_data=case["extract_data"])



if __name__ == '__main__':
    unittest.main()
