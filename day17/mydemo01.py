import unittest
from BeautifulReport import  BeautifulReport
import unittestreport
from unittestreport import TestRunner

su = unittest.defaultTestLoader.discover(start_dir='.', pattern='demo*.py')

runner = TestRunner(
    suite=su,
    filename="py52report.html",
    report_dir="./reports",
    title='接口测试报告',
    tester="海蛎",
    desc="上课项目测试生成的报告",
    templates=2
)

runner.run()
runner.send_email(host="smtp.qq.com",
                  port=465,
                  user="xiaoming")