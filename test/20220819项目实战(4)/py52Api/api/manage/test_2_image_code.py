"""
============================
Project: py52Api
Author:柠檬班-海励
Time:2022/8/15 20:56
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""

http://mall.lemonban.com:8108/captcha.jpg?uuid=a526d450-493c-4485-8262-dddc624b6208
uuid: a526d450-493c-4485-8262-dddc624b6208

http://api.ttshitu.com/predict

解析图片验证码


def base64_api(uname, pwd, img, typeid):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""

"""
import requests
import base64
import json

class ImageCode:

    def __init__(self):
        #图片地址
        self.image_url = "http://mall.lemonban.com:8108/captcha.jpg"
        #解析图片验证码的地址
        self.image_code_url = "http://api.ttshitu.com/predict"

    #获取图片
    def get_image(self,uuid):
        data = {"uuid":uuid}
        resp = requests.get(url=self.image_url,params=data)
        image_byte = resp.content# 获取响应结果的二进制
        base64_data = base64.b64encode(image_byte)
        b64 = base64_data.decode()
        return b64

    #解析图片
    def get_image_code(self,uuid):
        #请求图鉴的接口，解析图片验证码，将验证码返回
        #获取图片验证码的b64数据
        b64 = self.get_image(uuid=uuid)
        data = {"username": "haili", "password": "QINHAILI", "typeid": "3", "image": b64}
        resp = json.loads(requests.post(url=self.image_code_url,json=data).text)
        if resp['success']:
            return resp["data"]["result"]
        else:
            return resp["message"]
