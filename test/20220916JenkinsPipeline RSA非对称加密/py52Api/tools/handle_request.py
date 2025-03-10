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
import re
import requests
from requests_toolbelt import MultipartEncoder

from conf.setting import host_info
from tools.handle_attribute import HandleAttr
from tools.handle_path import image_dir
from tools.handle_response import HandleResponse


class HandleRequest:
    """
    1、获取登陆的token，设置到请求头里面去
    2、兼容普通的请求，也要兼容图片上传的请求


    """
    def __init__(self):
        self.headers = {"locale": "zh_CN"}
        self.response = HandleResponse()


    def __handle_url(self,url:str,port:str):
        if url.startswith("http"):
            print("是全路径，不需要拼接url")
        else:
            if port:
                url = host_info["host"] + str(port) + url
                print("需要拼接url")
            else:
                print("excel中port字段为空，请检查")
        key_list = re.findall("#(\w.+?)#",url)
        if len(key_list)>0:
            for key in key_list:
                if hasattr(HandleAttr,key):
                    url = url.replace(f"#{key}#",getattr(HandleAttr,key))
                else:
                    print(f"{key}在全局变量中不存在，无法替换url参数")
        else:
            print("url中不需要替换参数")
        return url

    #token鉴权处理
    def __handle_headers(self):
        if hasattr(HandleAttr,"access_token"):
            token = getattr(HandleAttr,"access_token")
            self.headers["Authorization"] =f"bearer{token}"
        else:
            print("全局属性中没有access_token属性，该接口不需要鉴权")


    #图片上传的请求
    def __upload_file(self,url):
        try:
            with open(file=image_dir, mode="rb") as file:
                image = file.read()
                data = MultipartEncoder(fields={
                    "file": ("py52.png", image, "image/png")
                })
                self.headers["Content-Type"] = data.content_type
                print(self.headers)
                resp = requests.post(url=url, data=data, headers=self.headers)
                print("图片上传响应：", resp.text)
                return resp
        except Exception as e:
            print("图片上传报错",e)
            return {}
        finally:
            self.headers["Content-Type"] = "application/json; charset=UTF-8"

    #发送请求
    def send_request(self,is_upload,url,method,data,port):
        #鉴权处理
        self.__handle_headers()
        #url地址处理
        url = self.__handle_url(url=url,port=port)
        if  is_upload == 1:
            print("图片上传接口")
            #图片上传接口
            resp = self.__upload_file(url=url)
        else:
            print("普通接口")
            #普通接口发请求
            resp = requests.request(method=method,url=url,json=data,headers=self.headers)
            print("普通接口响应:",resp.text)
        resp = self.response.handle_response(response=resp)
        return resp

