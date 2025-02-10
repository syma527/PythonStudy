"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/22 20:43
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
断言
self.assertEqual(1,1)
self.assertNotEqual()

self.assertIn()
self.assertNotIn()

self.assertFalse()
self.assertTrue()

self.assertIsNot()
self.assertIs()
"""

import unittest

class TestDemo3(unittest.TestCase):

    def test_11(self):
        print("test_01")
        self.assertEqual(1,1)

    def test_12(self):
        print("test_02")
        try:
            self.assertEqual(1, 2)
        except Exception as e:
            pass
            # raise AssertionError(f"test_12断言失败,{e}")


if __name__ == '__main__':
    unittest.main()




