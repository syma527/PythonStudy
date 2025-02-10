"""
============================
Project: py52Api
Author:柠檬班-海励
Time:2022/8/27 21:50
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""

import unittest
from ddt import data, ddt

from tools.handle_excel import HandleExcel
from tools.handle_path import case_data_dir

from tools.handle_replace import HandleReplace
from tools.handle_response import HandleResponse
from tools.handle_extract_data import HandleExtractData
from tools.handle_request import HandleRequest
from tools.handle_mysql import mysql
from tools.handle_assert_db import HandleAssertDb


# 从excel中拿到login页的测试数据
case_list = HandleExcel(file_name=case_data_dir, sheet_name="add_product").get_cases()


@ddt
class TestAddProduct(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.header = {"locale": "zh_CN"}
        cls.replace = HandleReplace()
        cls.response = HandleResponse()
        cls.extract = HandleExtractData()
        cls.request = HandleRequest()
        cls.assert_db = HandleAssertDb()

    @classmethod
    def tearDownClass(cls) -> None:
        mysql.close_db()

    @data(*case_list)
    def test_add_product(self, case):
        #替换请求参数
        data = self.replace.replace_data(data=case["data"])
        print("请求参数的数据类型:", type(data))
        #发请求
        response = self.request.send_request(is_upload=case["is_upload"],url=case["url"],method=case["method"],data=data)
        #接口断言
        self.response.assert_responsee(response=response, expected_data=case["expected_data"])
        #提取数据，设置为类属性
        self.extract.extract_data(response=response,extract_data=case["extract_data"])
        #数据库断言
        self.assert_db.assert_db(assert_db=case["assert_db"])

if __name__ == '__main__':
    unittest.main()
