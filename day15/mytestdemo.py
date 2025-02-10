import unittest

class TestDemo(unittest.TestCase):
    def test_01(self):
        print("这里是测试用例要做的事情")
        print("test_01")


    def test_02(self):
        print("test_02")


if __name__ == '__main__':
    #框架执行入口main函数，会自动收集测试用例
    unittest.main()