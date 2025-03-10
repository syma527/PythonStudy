"""
============================
Project: py52Api
Author:柠檬班-海励
Time:2022/8/19 20:03
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""


"""

下单流程

"""

import requests
import time


from api.mall.test_2_login import Login


class PlaceOrder:
    def __init__(self):
        #登陆鉴权
        self.headers = Login().login()

    # 获取秒杀订单地址
    def get_order_path(self):
        url = "http://mall.lemonban.com:8107/p/seckill/orderPath"
        resp = requests.get(url=url,headers=self.headers)
        print("获取秒杀订单地址:",resp.text)
        setattr(self,"order_path",resp.text)

    #创建订单
    def create_order(self):
        #获取秒杀订单地址
        self.get_order_path()
        url = "http://mall.lemonban.com:8107/p/seckill/{}/confirm".format(getattr(self,"order_path"))
        print(url)
        data = {
            "addrId": 0,
            "prodCount": 1,
            "seckillSkuId": 172
        }
        resp = requests.post(url=url,json=data,headers=self.headers)
        print("创建订单返回：",resp.text)

    #提交订单
    def commit_order(self):
        #创建订单
        self.create_order()
        #从属性拿秒杀订单的地址
        order_path = getattr(self, "order_path")
        url = "http://mall.lemonban.com:8107/p/seckill/{}/submit".format(order_path)
        data={
              "orderShopParam": {
                "remarks": "",
                "shopId": 1
              },
              "orderPath": order_path
            }
        resp = requests.post(url=url, json=data, headers=self.headers)
        print("提交订单返回：", resp.text)
        #获取响应结果中的orderNumbers
        orderNumbers = resp.json()["orderNumbers"]
        setattr(self,"orderNumbers",orderNumbers)
        print(self.__dict__)

    # 支付下单(用户扫码)
    def pay(self):
        self.commit_order()
        url = "http://mall.lemonban.com:8107/p/order/pay"
        data = {
                  "payType": 3,
                  "orderNumbers": getattr(self, "orderNumbers")
                }
        resp = requests.post(url=url, json=data, headers=self.headers)
        print("支付下单返回：", resp.text)


    # 模拟回调
    def call_back(self):
        #下单
        self.pay()
        url = "http://mall.lemonban.com:8107/notice/pay/3"
        data = {
                "payNo":getattr(self, "orderNumbers"), #商城支付订单号
                "bizPayNo":str(int(time.time()*1000)), #微信方的订单号
                "isPaySuccess":True,#True 成功，False 失败
                }
        resp = requests.post(url=url, json=data, headers=self.headers)
        print("回调返回：", resp.text)

if __name__ == '__main__':
    cl = PlaceOrder()
    cl.call_back()





