import unittest
import time

class TimeDemo(unittest.TestCase):

    def test_01(self):
        print("test_01")

    def test_02(self):
        print("test_01")
        time.sleep(1)

    def test_02(self):
        print("test_02")
        time.sleep(2)

    def test_03(self):
        print("test_03")
        time.sleep(3)

