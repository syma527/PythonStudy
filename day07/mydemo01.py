"""
一、字典排序
1.使用场景
数据加密传输，鉴权
敏感信息加密传输
rsa非对称加密
内部系统前后端交互（前端请求后端接口）
1、字典序，a--z
2、拿公钥进行加密，得到密串
3、传输带时候你只传密串过去
4、后端拿到你得数据，通过私钥解密

result = sorted(test_dict.items(),key = operator.itemgetter(1))
operator.itemgetter(1)
0:根据key排序
1：根据value排序
import operator
result = sorted(test_dict.items(),key = operator.itemgetter(0),reverse = true
print(dict(result))

"""
import operator

"""
def test(x):
    return x * 2


t1 = test(100)
print(t1)
res = lambda x: x * 3
t2 = res(100)
print(t2)
"""

test_dict = {"user": "root", "pwd": "123456", "code": "888888", "sign": "wesdnfslfngdfef"}
result = sorted(test_dict.items(), key=operator.itemgetter(1), reverse=False)
print(result)

"""
数据类型转换
一、能直接相互转换（样式是不会变化的）
34
"""

test_dict = {"user": "root", "pwd": "123456", "code": "888888", "sign": "sdsfdvnnv"}
result = sorted(test_dict.items(), key=operator.itemgetter(1), reverse=False)
print(result)
num = 100

if num == 10:
    print("num为%d" % (233))
else:
    print("num 为%d" %(23))
print(f"num 的值为{num}")
