"""
============================
Project: py52Api
Author:柠檬班-海励
Time:2022/8/19 20:47
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
import requests
import unittest
from ddt import data,ddt


from tools.handle_excel import HandleExcel
from tools.handle_path import case_data_dir

from tools.handle_replace import HandleReplace

#从excel中拿到login页的测试数据
case_list = HandleExcel(file_name=case_data_dir,sheet_name="login").get_cases()

@ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.header = {"locale": "zh_CN"}
        cls.replace = HandleReplace()

    @data(*case_list)
    def test_login(self,case):
        #替换请求参数
        data = self.replace.replace_data(data=case["data"])
        print("请求参数的数据类型:",type(data))
        #发请求
        resp = requests.request(method=case["method"],url=case["url"],json=data,headers=self.header)
        print(resp.text)


if __name__ == '__main__':
    unittest.main()


