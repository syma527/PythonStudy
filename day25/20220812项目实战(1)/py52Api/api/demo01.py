"""
============================
Project: py52Api
Author:柠檬班-海励
Time:2022/8/12 20:55
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、了解项目
1、商城项目，管理后端，商城端
2、接口类型：post请求、get请求、图片上传接口、图片验证码

二、找到核心业务
管理端：添加商品流程
商城端：购买商品(秒杀商品)

三、将核心业务流程每个接口都请求一遍
添加商品流程
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

2、图片上传
Request URL: http://mall.lemonban.com:8108/admin/file/upload/img
Request Method: POST
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryfiTjkFx67gFh7Ifl
------WebKitFormBoundaryfiTjkFx67gFh7Ifl
Content-Disposition: form-data; name="file"; filename="py52.png"
Content-Type: image/png
------WebKitFormBoundaryfiTjkFx67gFh7Ifl--

3、添加产品
Request URL: http://mall.lemonban.com:8108/prod/prod
Request Method: POST
Content-Type: application/json; charset=UTF-8
{      1660311777536
  "t": 1660311618690, #时间戳
  "prodName": "py52商品名称",
  "brief": "",
  "video": "",
  "prodNameEn": "py52商品名称",
  "prodNameCn": "py52商品名称",
  "contentEn": "",
  "contentCn": "<p><img src=\"https://img10.360buyimg.com/imgzone/jfs/t1/142476/27/23166/186549/614848d1Ee87e01cc/931c67cf16b3f9e0.jpg\" alt=\"描述1\" width=\"867\" height=\"1600\" /><img src=\"https://img10.360buyimg.com/imgzone/jfs/t1/109845/29/17835/167756/614848d1E824d0766/167f6932c38ee1b0.jpg\" alt=\"详情2\" width=\"990\" height=\"1128\" /></p>",
  "briefEn": "",
  "briefCn": "py52产品卖点",
  "pic": "2022/08/bd1ee80cd79345849ad7ecfddab84dcc.png",
  "imgs": "2022/08/bd1ee80cd79345849ad7ecfddab84dcc.png",
  "preSellStatus": 0,
  "preSellTime": null,
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
      "partyCode": "202208122135",#不能重复
      "prodNameCn": "py52商品名称",
      "prodNameEn": "py52商品名称"
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
    "hasShopDelivery": true,
    "hasUserPickUp": false,
    "hasCityDelivery": false
  }
}



商城端
select *from tz_attach_file where file_path = "2022/08/bd1ee80cd79345849ad7ecfddab84dcc.png";
select * from  tz_sms_log where user_phone = "13000000004"
注册账号
1、发送短信验证码
Request URL: http://mall.lemonban.com:8107/user/sendRegisterSms
Request Method: PUT
Content-Type: application/json; charset=UTF-8
{
  "mobile": "13000000004"
}

2、校验短信验证码
Request URL: http://mall.lemonban.com:8107/user/checkRegisterSms
Request Method: PUT
Content-Type: application/json; charset=UTF-8
{
  "mobile": "13000000004",
  "validCode": "835763"
}

3、注册
Request URL: http://mall.lemonban.com:8107/user/registerOrBindUser
Request Method: PUT
Content-Type: application/json; charset=UTF-8
{
  "appType": 3,
  "checkRegisterSmsFlag": "2be31a2afb594eee88cd58f8f6ff7f89",
  "mobile": "13000000004",
  "userName": "13000000004",
  "password": "123456",
  "registerOrBind": 1,
  "validateType": 1
}



"""
# import requests
# data = {
#   "t": 1660310530119,
#   "principal": "student",
#   "credentials": "123456",
#   "sessionUUID": "57cabe57-cc24-4e94-8a83-6917443bbb23",
#   "imageCode": "lemon"
# }
# # locale: zh_CN
# res = requests.post(url="http://mall.lemonban.com:8108/adminLogin",json=data,headers={"locale":"zh_CN"})
# print(res.text)

import time

print(int(time.time()*1000))



