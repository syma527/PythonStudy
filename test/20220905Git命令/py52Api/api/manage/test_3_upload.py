"""
============================
Project: py52Api
Author:柠檬班-海励
Time:2022/8/15 21:36
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""


"""
图片上传

安装包
pip install  requests-toolbelt
"""

import requests

from requests_toolbelt import MultipartEncoder

from api.manage.test_1_login import Login


class Upload:
    def __init__(self):
        #登陆
        self.login = Login()
        self.url = "http://mall.lemonban.com:8108/admin/file/upload/img"

    def upload(self):
        #登陆获取有鉴权的信息头
        headers = self.login.login()
        #读取图片，设置图片的请求头信息，获取图片的请求数据
        with open(file="D:\py52.png",mode="rb") as file:
            image = file.read()
            data = MultipartEncoder(fields={
                "file":("py52.png",image,"image/png")
            })
            headers["Content-Type"] = data.content_type
            print(headers)
            resp = requests.post(url=self.url,data=data,headers=headers)
            print("图片上传响应：",resp.text)

if __name__ == '__main__':
    cl = Upload()
    cl.upload()

test_str = "天朝"
print(test_str.isalnum())