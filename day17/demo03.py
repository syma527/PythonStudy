"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/25 20:35
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""

"""
数据驱动
一、安装第三方库
pip install ddt==1.5.0 -i http://mirrors.aliyun.com/pypi/simple/

二、使用
什么是数据驱动，为什么要用数据驱动，什么场景适合用数据驱动？
同一个接口(登陆页面测试)
1、登陆成功
2、登陆失败：密码错误
3、登陆失败：账号错误
4、登陆失败：账号密码不匹配
相同点：
1、请求的接口是一样的
2、请求方法是一样的
3、请求头信息
不同点：
1、请求参数不一样

不同接口
相同点：
1、鉴权方式(统一系统)
2、协议是一样的(http)
3、域名(ip)
不同点：
1、接口地址不一样   pass
2、请求参数不一样   pass
3、请求方法不一样   pass
4、请求头不一样(请求参数的编码方式)  pass


三、使用
语法
from ddt import ddt,data
@ddt
class Test:
    @data(*test_data)
    def test_01(self,case):
       pass

"""

import requests
import unittest
from ddt import ddt, data

test_data = [
    {"method": "post", "title": "登陆成功1", "url": "https://www.lemon.com/login1"},
    {"method": "get", "title": "登陆成功2", "url": "https://fanyi.youdao.com/#/TextTranslate"},
    {"method": "patch", "title": "登陆成功3", "url": "https://www.lemon.com/login3"}
]


class TestDemo4(unittest.TestCase):

    @data(*test_data)  # 解压数据
    def test_01(self, case):
        print("拿着请求参数去发请求", type(case))
        res = requests.request(method=case["method"], url=case["url"])
        print(res)



if __name__ == '__main__':
    unittest.main()
