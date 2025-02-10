import unittest

class Testunit(unittest.TestCase):
    def setUp(self):
        print("前置函数执行")

    @classmethod
    def setUpClass(cls):
        print("在类前置执行")

    def tearDown(self):
        print("函数后执行")

    @classmethod
    def tearDownClass(cls):
        print("在类之后执行")

    def test01(self):
        print("这是函数1")

    def test02(self):
        print("这是函数2")


if __name__ == '__main__':
    unittest.main()