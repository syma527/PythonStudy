"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/1 19:49
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""

"""
六、字典排序
1、使用场景
数据加密传输，鉴权
敏感信息做加密传输

RSA非对称加密
内部系统前后端交互(前端请求后端接口)
1、字典序，a--z
2、拿公钥进行加密，得到密串
3、传输的时候你只传密串传过去
4、后端拿到你的数据，通过私钥解密
请求参数：{"user":"root","pwd":"123456","code":"888888"}
实际传给后端的参数：{"data":"hP7xEyAGRu/MZjKncRLDzkIo39J6fcWmnKtjhrMVZxTlbWmoqZ3GSte0IUoz7/Sba83m7LjX/8cnPVRZi4K6g4uHBnven0O4QpLlQftTRRTJjWpEUjSBNRMf+IqHBCNgjdlB0W6keKla1z7UlB9WNZUC0uIwJgiFUU7ayEyluhs=


鉴权
接口对外部公司开放
1、字典序，a--z
2、拿到这个排序后的字典去签名(公钥)，得到签名的串
3、传输的时候，
请求参数：{"user":"root","pwd":"123456","code":"888888"}
实际传给后端的参数：{"user":"root","pwd":"123456","code":"888888","sign":"hP7xEyAGRu/MZjKncRLDzkIo39J6fcWmnKtjhrMVZxTlbWmoqZ"}


二、怎么排序
result = sorted(test_dict.items(),key=operator.itemgetter(1))
operator.itemgetter(1)
0: 根据key排序
1: 根据value排序s
import operator
result = sorted(test_dict.items(),key=operator.itemgetter(0),reverse=True)
# 通过operator。itemgetter获取items，然后去遍历item。如果是0 根据key排序，如果是1 根据value排序，reverse = true
print(dict(result))


三、拓展测开内容
#普通函数
def test(x):
    return x*2
t1 = test(100)
print(t1)
#匿名函数
res = lambda x:x*2
t2 = res(100)
print(t2)

#lambda实现 [('user', 'root'), ('pwd', '123456'), ('code', '888888')]
result = sorted(test_dict.items(),key=lambda x:x[0],reverse=True)
print(dict(result))

# 嵌套list排序
test_list = [[22,3,33],[10,4,3],[2,1,63]]
new_list = sorted(test_list,key=lambda x:x[2],reverse=True)
print(new_list)
test_list.sort(key=lambda x:x[2])
print(test_list)

"""


test_dict = {"user":"root","pwd":"123456","code":"888888"}

# import operator
# test_dict.items()  =  [('user', 'root'), ('pwd', '123456'), ('code', '888888')]
# result = sorted(test_dict.items(),key=operator.itemgetter(0),reverse=True)
# print(dict(result))

#普通函数
def test(x):
    return x*2
t1 = test(100)
print(t1)
#匿名函数
res = lambda x:x*2
t2 = res(100)
print(t2)


#lambda实现 [('user', 'root'), ('pwd', '123456'), ('code', '888888')]
result = sorted(test_dict.items(),key=lambda x:x[0],reverse=True)
print(dict(result))


# 嵌套list排序
test_list = [[22,3,33],[10,4,3],[2,1,63]]
new_list = sorted(test_list,key=lambda x:x[2],reverse=True)
print(new_list)
test_list.sort(key=lambda x:x[2])
print(test_list)