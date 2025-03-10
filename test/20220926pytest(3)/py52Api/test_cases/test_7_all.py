"""
============================
Project: py52Api
Author:柠檬班-海励
Time:2022/9/2 21:20
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
测试用例


"""
import unittest
from ddt import data, ddt



from tools.handle_replace import HandleReplace
from tools.handle_response import HandleResponse
from tools.handle_extract_data import HandleExtractData
from tools.handle_request import HandleRequest
from tools.handle_assert_db import HandleAssertDb
from tools.handle_setup_sql import HandleSetupSql


def generator_case_class(case_list):
    @ddt
    class TestAll(unittest.TestCase):

        @classmethod
        def setUpClass(cls) -> None:
            cls.header = {"locale": "zh_CN"}
            cls.replace = HandleReplace()
            cls.response = HandleResponse()
            cls.extract = HandleExtractData()
            cls.request = HandleRequest()
            cls.assert_db = HandleAssertDb()
            cls.setup_sql = HandleSetupSql()

        @data(*case_list)
        def test_all(self, case):
            #执行前置sql语句
            self.setup_sql.setup_sql(sql_list=case["setup_sql"])
            #替换请求参数
            data = self.replace.replace_data(data=case["data"])
            print("请求参数的数据类型:", type(data))
            #发请求
            response = self.request.send_request(is_upload=case["is_upload"],url=case["url"],method=case["method"],data=data,port=case["port"])
            #接口断言
            self.response.assert_responsee(response=response, expected_data=case["expected_data"])
            #提取数据，设置为类属性
            self.extract.extract_data(response=response,extract_data=case["extract_data"])
            #数据库断言
            self.assert_db.assert_db(assert_db=case["assert_db"])

    return TestAll
if __name__ == '__main__':
    unittest.main()
