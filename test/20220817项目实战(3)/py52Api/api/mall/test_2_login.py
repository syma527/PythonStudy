"""
============================
Project: py52Api
Author:柠檬班-海励
Time:2022/8/17 21:48
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
商城端登陆
Request URL: http://mall.lemonban.com:8107/login
Request Method: POST
Content-Type: application/json; charset=UTF-8
{
  "principal": "18820992515",
  "credentials": "123456",
  "appType": 3,
  "loginType": 0
}

"""
import requests
from jsonpath import jsonpath
from api.mall.data import Data
from api.mall.test_1_register import Register

class Login:
    def __init__(self):
        self.headers = {}
        self.login_url = "http://mall.lemonban.com:8107/login"
        Register().start() #注册账号

    def login(self):
        data = {
            "principal": getattr(Data,"phone"),
            "credentials": "123456",
            "appType": 3,
            "loginType": 0
        }
        resp = requests.post(url=self.login_url,json=data)
        print("登陆接口返回：",resp.text)
        token = jsonpath(resp.json(),"$..access_token")[0]
        self.headers["Authorization"] =f"bearer{token}"
        print("加了鉴权的请求头：",self.headers)
        return self.headers

if __name__ == '__main__':
    cl = Login()
    cl.login()




