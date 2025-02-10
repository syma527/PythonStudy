"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/22 20:35
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
二、用例执行顺序
1、按照测试用例名称ASCII码大小来执行(ASCII码小的先执行)
2、逐位比对大小(ASCII码)
3、ord("a")获取ascii码
4、chr(97)通过ascii码获取对应的值


"""

import unittest


class TestDemo2(unittest.TestCase):

    def test_13(self):
        print("test_01")

    def test_12(self):
        print("test_02")


if __name__ == '__main__':
    unittest.main()

