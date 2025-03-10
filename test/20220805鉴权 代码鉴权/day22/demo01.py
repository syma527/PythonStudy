"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/8/5 20:09
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、鉴权
1、cookie鉴权：不适合放太多东西，太大的东西，这种被淘汰了，放在浏览器缓存里面，不安全
2、session(session+cookie)：sessionid(存数据库)，耗存储空间
3、token(通过算法实现)：加密算法拿用户各种信息按规则生成一个字符串(令牌)，返回给客户端
开放鉴权：对外接口通过授权访问的方式进行鉴权(请求参数rsa加密+授权接口返回给你令牌)

二、session鉴权
1、提交用户名和密码(用户信息)进行注册
2、后端会校验用户是否注册过(用户名是否重复)，未注册就会将用户信息落库
3、登陆：提交用户名+密码，后端校验是否有这个用户(查询数据库校验用户名和密码)，
   创建session，那用户信息或者用户id创建一个字符串(哈希)，将字符串设置到数据库(redis、mongoDB)
   {"seddion_id":"hhhjsjdhfasjdhfjaskdhfaksjdhfkasd;kjlksdjlfajdlfa"}
   将session_id返回给客户端，通过Set-cookie字段返回
4、客户端接收到数据，获取Set-cookie的值，下一次请求的时候，将请求头Set-cookie的值设置一下
5、后端收到第二个请求，解析出session_id，然后去数据库中去获取对应的值，进行校验


三、token鉴权
1、登陆提交用户信息，后端先校验用户名和密码是否正确，通过可逆算法进行加密生成token(拿可以区分用户唯一性的id)
2、后端将token放到响应体或者响应头返回给前端，前端拿到之后将token 按要求放到请求头里面，继续请求其他接口
3、后端收到第二个请求，解析出token，解密出token中的数据，获取到用户唯一性标识的数据和时间戳，判断用户token是否合法，是否token 超时了


四、实战token鉴权
import requests

url1 = "http://mall.lemonban.com:8108/adminLogin"
data = {
          "t": 1659703169926,
          "principal": "student",
          "credentials": "123456a",
          "sessionUUID": "9422def8-1a5a-412ed-8041-f0b1c73e5ed5",
          "imageCode": "lemon"
        }
res = requests.post(url=url1,json=data)
token = res.json()["access_token"] #字典取值

headers = {"Authorization": f"bearer{token}"}
url2 = "http://mall.lemonban.com:8108/sys/webConfig/getActivity"
res2 = requests.get(url=url2,headers=headers)
print(res2.json())


"""

import requests

def login():
    url1 = "http://mall.lemonban.com:8108/adminLogin"
    data = {
              "t": 1659703169926,
              "principal": "student",
              "credentials": "123456a",
              "sessionUUID": "9422def8-1a5a-412ed-8041-f0b1c73e5ed5",
              "imageCode": "lemon"
            }
    res = requests.post(url=url1,json=data)
    print(res.json())
    token = res.json()["access_token"] #字典取值
    return token

def get_message():
    token = login()
    headers = {"Authorization": f"bearer{token}"}
    url2 = "http://mall.lemonban.com:8108/sys/webConfig/getActivity"
    res2 = requests.get(url=url2,headers=headers)
    print(res2.json())


get_message()
