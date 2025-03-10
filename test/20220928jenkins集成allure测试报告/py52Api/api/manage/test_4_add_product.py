"""
============================
Project: py52Api
Author:柠檬班-海励
Time:2022/8/17 20:10
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
添加产品




"""
import time
import requests
from api.manage.test_1_login import Login


class AddProduct:
    def __init__(self):
        #登陆获取请求头
        self.headers = Login().login()
        self.pro_url = "http://mall.lemonban.com:8108/prod/prod"

    #添加产品
    def add_product(self):
        data = {
                  "t": int(time.time()*1000), #时间戳
                  "prodName": "秒杀商品测试",
                  "brief": "",
                  "video": "",
                  "prodNameEn": "秒杀商品测试",
                  "prodNameCn": "秒杀商品测试",
                  "contentEn": "",
                  "contentCn": "<p><img src=\"https://img10.360buyimg.com/imgzone/jfs/t1/142476/27/23166/186549/614848d1Ee87e01cc/931c67cf16b3f9e0.jpg\" alt=\"描述1\" width=\"867\" height=\"1600\" /><img src=\"https://img10.360buyimg.com/imgzone/jfs/t1/109845/29/17835/167756/614848d1E824d0766/167f6932c38ee1b0.jpg\" alt=\"详情2\" width=\"990\" height=\"1128\" /></p>",
                  "briefEn": "",
                  "briefCn": "秒杀商品测试卖点",
                  "pic": "2022/08/bd1ee80cd79345849ad7ecfddab84dcc.png",
                  "imgs": "2022/08/bd1ee80cd79345849ad7ecfddab84dcc.png",
                  "preSellStatus": 0,
                  "preSellTime": None,
                  "categoryId": 283,
                  "skuList": [
                    {
                      "price": 0.01,
                      "oriPrice": 0.01,
                      "stocks": 10000,
                      "skuScore": 1,
                      "properties": "",
                      "skuName": "",
                      "prodName": "",
                      "weight": 22,
                      "volume": 23,
                      "status": 1,
                      "partyCode": int(time.time()*1000),#不能重复
                      "prodNameCn": "秒杀商品测试",
                      "prodNameEn": "秒杀商品测试"
                    }
                  ],
                  "tagList": [
                    1
                  ],
                  "content": "",
                  "deliveryTemplateId": 1,
                  "totalStocks": 10000,
                  "price": 0.01,
                  "oriPrice": 0.01,
                  "deliveryModeVo": {
                    "hasShopDelivery": True,
                    "hasUserPickUp": False,
                    "hasCityDelivery": False
                  }
                }

        resp = requests.post(url=self.pro_url,json=data,headers=self.headers)
        print(resp.json())

if __name__ == '__main__':
    cl = AddProduct()
    cl.add_product()





