"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/8/3 20:51
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
二、requests库的使用
1、安装
pip install requests==2.24.0

2、概念
   1、接口：用于传递数据的通道就叫接口
   2、接口请求相当于什么操作：去掉客户端+nginx服务器，去请求后端服务器

3、requests库有哪些方法
   1、get
   2、post
   3、put
   4、patch

4、get请求
4.1、get请求参数通过params关键字传递，也可以放到接口地址后面传递
4.2、接口地址后面放参数，通过?key1=val1&key2=val2
import requests
import pprint
url="http://httpbin.org/get?key1=val1&key2=val2"
res = requests.get(url=url,params={"key3":"val3"})
print(pprint.pprint(res.json()))

5、post
5.1、data关键字接收form表单个数的数据(表单数据，key=val,key2=val2)
     默认：'Content-Type': 'application/x-www-form-urlencoded'
     设置请求头={'Content-Type': 'application/json'}
     参数通过data关键字传递
5.2、json关键字接收数据(jsonstr)
     默认：'Content-Type': 'application/json'
     设置请求头={'Content-Type': 'application/x-www-form-urlencoded'}
     参数会使用表达格式去传递，通过form关键字传参
     
     
     
import requests
import pprint
head={'Content-Type': 'application/json'}
url="http://httpbin.org/post"
# data=None, json=None
value = {"key3":"val3"}
res = requests.post(url=url,data=value,headers=head)
print(pprint.pprint(res.json()))


6、举例
import requests
url = "http://mall.lemonban.com:8108/adminLogin"
data = {
  "t": 1659533726882,
  "principal": "student",
  "credentials": "123456a",
  "sessionUUID": "38e08041-d2bb-4006-876c-a37311b005e9",
  "imageCode": "lemon"
}
res = requests.post(url= url,json=data)
print(res.json())

7、获取请求相关的数据
print(res.request.url)
print(res.request.method)
print(res.request.body)
print(res.request.headers)

"""



import requests
url = "http://mall.lemonban.com:8108/adminLogin"
data = {
  "t": 1659533726882,
  "principal": "student",
  "credentials": "123456a",
  "sessionUUID": "38e08041-d2bb-4006-876c-a37311b005e9",
  "imageCode": "lemon"
}
res = requests.request(method="post",url=url,json=data)
# print(res.json())

#请求相关的数据
# print(res.request.url)
# print(res.request.method)
# print(res.request.body)
# print(res.request.headers)


#响应相关的数据
print(res.json()) #只能解析json格式的数据,字典dict = {"key":"val"}
print(res.text) # 通用，可以解析所有格式数据
print(res.cookies)




