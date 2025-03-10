"""
============================
Project: py52Api
Author:柠檬班-海励
Time:2022/8/29 15:43
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""

"""

-- 秒杀活动剩余库存
update tz_seckill set seckill_total_stocks=100,seckill_origin_stocks=1000,is_delete=0,status=1,start_time = '2022-08-30 00:00:00',end_time = '2023-08-30 00:00:00' where seckill_id = 133;

-- 秒杀商品库存设置为1000
update tz_sku set actual_stocks = 1000 where prod_id = 2452;

-- 商品总库存调整为1000
update tz_prod set total_stocks=10000 where prod_id = 2452;

-- 用于秒杀的库存
update tz_seckill_sku set seckill_stocks=1000;

"""


import pymysql
import time
import uuid
import requests
from jsonpath import jsonpath
class AddSeckillProduct:
    def __init__(self):
        self.headers = {"locale": "zh_CN"}
        self.login_url = "http://mall.lemonban.com:8108/adminLogin"
        self.db = pymysql.connect(
                        host="47.113.180.81",
                        port=3306,
                        user="lemon",
                        password="lemon123",
                        db="yami_shops",
                        autocommit=True,
                        charset="utf8",
                        cursorclass=pymysql.cursors.DictCursor
                        )

        self.cur = self.db.cursor()
        self.execute_sql()

    def execute_sql(self):
        try:
            sql = "select sku_id,prod_id,prod_name,party_code from tz_sku where party_code is not null and status=1  and  properties = '' and is_delete=0 and  prod_name != '' and  prod_id in (select prod_id from tz_prod where total_stocks >10 and status = 1 and seckill_activity_id = 0 and is_compose = 0) and sku_id not in (select sku_id from tz_seckill_sku ) order by prod_id desc limit 1"
            print(sql)
            self.cur.execute(sql)
            product_info = self.cur.fetchall()[0]
            print(product_info)
            for key,val in product_info.items():
                setattr(self,key,val)
        except Exception as e:
            print("数据库查询报错")
        finally:
            self.cur.close()
            self.db.close()

    def login(self):
        my_uuid = str(uuid.uuid4())
        data = {
            "t": int(time.time() * 1000),
            "principal": "student",
            "credentials": "123456a",
            "sessionUUID": my_uuid,
            "imageCode": "lemon"
        }
        print("请求参数：", data)
        resp = requests.post(url=self.login_url, json=data, headers=self.headers)
        print("登陆响应：", resp.json())
        token = jsonpath(resp.json(), "$..access_token")[0]
        self.headers["Authorization"] = f"bearer{token}"


    def add_seckill_product(self):
        self.login()
        url = "http://mall.lemonban.com:8108/seckill/seckill"
        seckill_name = f"python专用秒杀商品{int(time.time() * 1000)}"
        data = {
          "t": int(time.time()*1000),
          "dateRange": [
            "2022-08-29 00:00:00",
            "2032-09-29 00:00:00"
          ],
          "seckillId": 0,
          "seckillName":seckill_name,
          "startTime": "2022-08-29 00:00:00",
          "endTime": "2032-09-29 00:00:00",
          "seckillTag": "python自动化专用",
          "maxNum": -1,
          "hasMaxNum": 0,
          "maxCancelTime": 2,
          "price": None,
          "stocks": None,
          "prodId": int(getattr(self,"prod_id")),
          "seckillSkus": [
            {
              "skuId": int(getattr(self,"sku_id")),
              "prodId": int(getattr(self,"prod_id")),
              "properties": "",
              "propertiesEn": None,
              "oriPrice": 0.01,
              "price": 0.01,
              "stocks": 10000,
              "actualStocks": None,
              "updateTime": "2022-08-17 20:18:32",
              "recTime": "2022-08-17 20:18:32",
              "partyCode": getattr(self,"party_code"),
              "modelId": None,
              "pic": None,
              "skuName": "",
              "skuNameEn": None,
              "prodName": getattr(self,"prod_name"),
              "version": None,
              "weight": 22,
              "volume": 23,
              "status": 1,
              "isDelete": 0,
              "skuScore": 1,
              "prodNameCn": None,
              "prodNameEn": None,
              "skuLangList": [
                {
                  "skuId": int(getattr(self,"sku_id")),
                  "lang": 0,
                  "properties": "",
                  "skuName": "",
                  "prodName": getattr(self,"prod_name")
                },
                {
                  "skuId": int(getattr(self,"sku_id")),
                  "lang": 1,
                  "properties": None,
                  "skuName": None,
                  "prodName": getattr(self,"prod_name")
                }
              ],
              "skuSingleProds": None,
              "seckillPrice": 0.01,
              "seckillStocks": 10000
            }
          ]
        }
        print('请求参数：',data)
        resp = requests.post(url=url, json=data, headers=self.headers)
        print("添加秒杀产品返回:",resp.text)

if __name__ == '__main__':
    cl = AddSeckillProduct()
    cl.add_seckill_product()


