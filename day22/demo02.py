"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/8/5 21:25
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
五、session鉴权
第一种：手动添加cookie
#登陆接口
url1 = "https://v4.ketangpai.com/UserApi/login"
data1 = {"email":"1605118090@qq.com",
        "password":"Aa123456",
         "remember":0}
res1 = requests.post(url=url1,data=data1)
#获取cookie
cookie = res1.headers["Set-Cookie"]

url2 = "https://v4.ketangpai.com/VipApi/isVip"
data2 = {"email":"1605118090@qq.com",
        "password":"Aa123456",
         "remember":0}
#添加cookie鉴权
res2 = requests.get(url=url2,headers={"cookie":cookie})
print(res2.json())

第二种：自动添加cookie【推荐】
import requests
#创建会话
session = requests.session()
#登陆接口
url1 = "https://v4.ketangpai.com/UserApi/login"
data1 = {"email":"1605118090@qq.com",
        "password":"Aa123456",
         "remember":0}
res1 = session.post(url=url1,data=data1)
print(res1.json())
cookie = res1.headers["Set-Cookie"]
print("="*30)
print(cookie)
url2 = "https://v4.ketangpai.com/VipApi/isVip"
data2 = {"email":"1605118090@qq.com",
        "password":"Aa123456",
         "remember":0}
#添加cookie鉴权
res2 = session.get(url=url2)
print(res2.json())
#获取请求头
print(res2.request.headers)

"""
import requests
#创建会话
session = requests.session()
#登陆接口
url1 = "https://v4.ketangpai.com/UserApi/login"
data1 = {"email":"1605118090@qq.com",
        "password":"Aa123456",
         "remember":0}
res1 = session.post(url=url1,data=data1)
print(res1.json())
cookie = res1.headers["Set-Cookie"]
print("="*30)
print(cookie)
url2 = "https://v4.ketangpai.com/VipApi/isVip"
data2 = {"email":"1605118090@qq.com",
        "password":"Aa123456",
         "remember":0}
#添加cookie鉴权
res2 = session.get(url=url2)
print(res2.json())
#获取请求头
print(res2.request.headers)




