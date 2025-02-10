import requests
import unittest

from ddt import ddt,data
test_data = [
    {"method":"post","title":"登录成功1","url":"http://www.lemon.com/login1"},
    {"method":"get","title":"登录成功2","url":"http://www.lemon.com/login2"},
    {"method":"patch","title":"登录成功3","url":"http://www.lemon.com/login3"}
]
@ddt
class TestDemo4(unittest.TestCase):

    @data(*test_data)
    def test_01(self,case):
        print("拿着请求参数去发请求",type(case))
        res = requests.request(method=case["method"],url=case["url"])
        print(res)

if __name__ == '__main__':
    unittest.main()