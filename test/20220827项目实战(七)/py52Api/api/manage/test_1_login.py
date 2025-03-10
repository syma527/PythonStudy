"""
============================
Project: py52Api
Author:柠檬班-海励
Time:2022/8/15 20:33
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""


"""

1、登陆接口
Request URL: http://mall.lemonban.com:8108/adminLogin
Request Method: POST
Content-Type: application/json; charset=UTF-8
{
  "t": 1660310530119,
  "principal": "student",
  "credentials": "123456a",
  "sessionUUID": "57cabe57-cc24-4e94-8a83-6917443bbb23",
  "imageCode": "lemon"
}


"""
import requests
import time
import uuid
from jsonpath import jsonpath
from api.manage.test_2_image_code import ImageCode

class Login:
    def __init__(self):
        self.headers = {"locale": "zh_CN"}
        self.login_url = "http://mall.lemonban.com:8108/adminLogin"
        self.get_image_code = ImageCode()

    def login(self):
        my_uuid = str(uuid.uuid4())
        #获取图片验证码
        # image_code = self.get_image_code.get_image_code(uuid = my_uuid)
        data = {
            "t": int(time.time()*1000),
            "principal": "student", #账号
            "credentials": "123456a", #密码
            "sessionUUID": my_uuid, #会话UUID 不能重复每次都是唯一的
            "imageCode": "lemon" #万能验证码,最好通过万能验证码解决，通过第三方图片识别平台去处理
            #"imageCode": image_code #万能验证码,最好通过万能验证码解决，通过第三方图片识别平台去处理
        }
        print("请求参数：",data)
        resp = requests.post(url=self.login_url,json=data,headers={"locale":"zh_CN"})
        print("登陆响应：",resp.json())
        token = jsonpath(resp.json(),"$..access_token")[0]
        self.headers["Authorization"] =f"bearer{token}"
        print(self.headers)
        return self.headers

if __name__ == '__main__':
    cl = Login()
    cl.login()
    # print(int(time.time()*1000))
    # print(str(uuid.uuid4()),type(uuid.uuid4()))




