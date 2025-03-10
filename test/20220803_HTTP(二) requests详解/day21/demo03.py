"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/8/3 21:57
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
三、鉴权
cookie鉴权：不适合放太多东西，太大的东西，这种被淘汰了，放在浏览器缓存里面，不安全
session(session+cookie)：sessionid(存数据库)，耗存储空间
token(通过算法实现)：加密算法拿用户各种信息按规则生成一个字符串(令牌)，返回给客户端
开放鉴权：对外接口通过授权访问的方式进行鉴权(请求参数rsa加密+授权接口返回给你令牌)

"""