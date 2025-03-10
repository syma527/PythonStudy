"""
============================
Project: py52Api
Author:柠檬班-海励
Time:2022/8/24 21:58
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
import requests
class HandleRequest:
    """
    1、获取登陆的token，设置到请求头里面去
    2、兼容普通的请求，也要兼容图片上传的请求


    """


    #图片上传的请求
    def upload_file(self):
        pass

    #发送请求
    def send_request(self):
        if  判断是否是文件上传请求:
            #图片上传接口
            self.upload_file()
        else:
            #普通接口发请求
            requests.request()