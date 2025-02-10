import unittest

class TestDemo3(unittest.TestCase):

    def test_11(self):
        print("test_01")
        self.assertEqual(1,1)

    def test_12(self):
        print("test_02")
        try:
            self.assertEqual(2,3)
        except Exception as e:
            pass

if __name__ == '__main__':
    unittest.main()