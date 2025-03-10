"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/8/1 20:09
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
HTTP
一、OSI模型
1、七层网络模型
2、五层网络模型
3、TCP三次握手四次挥手
http://testingpai.com/article/1621669379653
http://testingpai.com/article/1647511749166

二、http协议
1、超文本传输协议，用于服务器之间传输文本和数据使用的传输规范
2、http协议基于TCP协议之上的协议，默认端口是80端口
   车子 --- http协议
   高速公路 --- tcp协议
3、http协议值关注是否按照我的协议规则来使用，不关心传输的内容

三、http常用方法
1、get：向服务器获取资源【掌握】
2、post：向服务器提交资源【掌握】
3、delete：删除资源
4、option：查询接口支持的请求方法
5、trace：测试用例，看接口是否请求通，还请求数据
6、put：修改资源，全部修改{“key1”：“val1”，“key2”：“val1”} == {“key1”：“val88”，“key2”：“val1”}【掌握】
7、patch：修改资源，部分修改{“key1”：“val88”}  == {“key1”：“val88”，“key2”：“val1”}
8、head: 查询响应头
9、connect：http/1.1协议预留的方法，代理服务器，代替用户去访问数据(网站接口)，拿到数据后再返回数据

四、http报文【掌握】
1、接口请求的四件套
Request URL: http://mall.lemonban.com:8108/adminLogin
Request Method: POST
Content-Type: application/json; charset=UTF-8
{
  "t": 1659356320671,
  "principal": "student",
  "credentials": "123456a",
  "sessionUUID": "1aba122e-0a54-4c4a-841f-8701d1b1a964",
  "imageCode": "lemon"
}


2、请求头【用来和服务器进行协商通信的规则】【了解】
告诉服务端，客户端能处理的内容的类型
Accept: application/json, text/plain, */*
告诉服务端，客户端支持的编码格式(压缩算法)
Accept-Encoding: gzip, deflate
告诉服务端，客户端可以处理的自然语言(中文、英文)
Accept-Language: zh-CN,zh;q=0.9
项目自定义的，鉴权字段
Authorization: null
告诉服务端是否关闭当前连接(http是有状态的)
Connection: keep-alive
请求体的长度
Content-Length: 138
告知服务端，客户端使用json数据格式进行编码，接口文档里面一定会有的
Content-Type: application/json;charset=UTF-8 【掌握】
前端(浏览器)本地缓存数据
Cookie: JSESSIONID=0267E92C58153FD19A9F33F5C3CB7F0C
访问的远程服务器的域名和端口
Host: mall.lemonban.com:8108
项目自定义的，控制接口返回数据的自然语言(中文，自动获取系统语言)
locale: zh_CN
远程地址
Origin: http://mall.lemonban.com
告诉服务端，用户代理信息(用的什么软件请求我服务器的)
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36

3、响应头【了解】
告诉客户端，响应的数据是否可以暴露给页面展示
Access-Control-Allow-Credentials: true
请求资源只能被mall.lemonban.com域名来访问
Access-Control-Allow-Origin: http://mall.lemonban.com
客户端缓存策略(客户端是否要缓存服务端发给你的数据)
Cache-Control: no-cache, no-store, max-age=0, must-revalidate
告诉客户端是否关闭当前连接(http是有状态的)
Connection: keep-alive
告诉客户端服务器能处理的数据编码格式，接口文档里面一定会有的
Content-Type: application/json;charset=UTF-8  【掌握】

4、请求体【了解】
请求参数

5、响应体【了解】
接口返回的数据

五、状态码【了解】
1、1xx: 服务端已经收到了你的请求，客户端还要继续操作
   100：客户端需要继续操作
   101：请求的http版本过低，需要换更高版本的http协议版本请求
2、2xx: 请求成功，用于正常的请求
   200：请求成功
   201：请求成功了，资源创建好了
   202：请求成功了，事情还没处理完成
   204：请求无内容，未返回任何内容
   206：请求成功，事情只办完了一部分，部分成功
3、3xx: 重定向，客户端访问的资源被移除了，或者是不存在这个链接了，会重定向到对应的资源的路径
   301：访问的资源已经被永久移除掉了，会返回一个替代的连接给你
   302：访问的资源已经被临时移除掉了，会返回一个替代的连接给你
   303：查看其他地址，返回其他接口地址给你
   304：资源没修改，不会给你数据，用于修改数据的接口返回
   307：临时重定向类似302
4、4xx: 客户端错误，请求数据和后端能处理的数据编码格式不一致，请求头设置错了
   401：需要身份认证
   403：服务端拒绝客户端的请求(请求没问题，但是不处理)
   404：服务端无法根据客户端的请求找到资源(接口地址可能错了)
   415：请求头错误，或者是请求参数错了(编码格式)
5、5xx: 服务端错误，服务端报错了，服务挂了  {"code":500,"msg":"请求参数错误"}
   500：服务端内部错误，无法完成请求
   501：服务端不支持的请求方式
   502：服务器作为网关去执行请求，但是收到了一个无效的响应
   503：服务器超负荷了，服务器在维护中，系统升级的时候
   504：服务器从其他地方去给你拿资源，但是超时了，没拿到(服务作为网关代替你去获取资源未获取到)
   505：服务器不支持你的http版本
   
六、RESTFul风格的api设计
{“status”:200,"msg":"success"}
{“status”:415,"msg":"请求数据有误"}

"""