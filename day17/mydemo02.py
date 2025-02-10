import unittest
from unittestreport import TestRunner
# 创建测试套件，用来收集测试用例
su = unittest.defaultTestloader.discover(start_dir=".", pattern='demo*.py')

runner = TestRunner(
        suite=su,
        filename="py52re",
        tester="xiaoming",
        desc="测试报告",
        templates=1
)