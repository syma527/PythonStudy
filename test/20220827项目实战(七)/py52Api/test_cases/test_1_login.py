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
from tools.handle_response import HandleResponse



#从excel中拿到login页的测试数据
case_list = HandleExcel(file_name=case_data_dir,sheet_name="login").get_cases()

@ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.header = {"locale": "zh_CN"}
        cls.replace = HandleReplace()
        cls.response = HandleResponse()

    @data(*case_list)
    def test_login(self,case):
        #替换请求参数
        data = self.replace.replace_data(data=case["data"])
        print("请求参数的数据类型:",type(data))
        #发请求
        resp = requests.request(method=case["method"],url=case["url"],json=data,headers=self.header)
        print('响应结果：',resp.text)
        #响应结果处理
        new_response = self.response.handle_response(response=resp)
        #接口断言
        self.response.assert_responsee(response=new_response,expected_data=case["expected_data"])




if __name__ == '__main__':
    unittest.main()



"""

{"access_token":"a8728d30-f954-4b2b-99a1-53074bc02e6a","token_type":"bearer","refresh_token":"ef9ce6ee-4e1b-4983-8693-27383c20993b","expires_in":1295999}

{"resp":账号或密码不正确}

{"resp":账号或密码不正确}


{"token_type":"bearer"}


"""









# import json
# test_str = """{"key":"val"}"""
# print(type(test_str))
# res = json.loads(test_str)
# print(type(res))
# print(res)
# test = [{"replace_key":['key1','key2'],"data":{"key1":"val","key2":"val"}},{"":"","":""}]




# test1 = {"token_type":"bearer","test1":"val1"}
# test2 = {"test1":"val1","token_type":"bearer"}
#
# print(test1 == test2)
# print(test1 is test2)



