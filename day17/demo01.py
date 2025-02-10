"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/25 20:14
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
1、2020年的最老的自动化课程邮件发送，继承在jenkins上发邮件
   问题：jenkins插件不稳定(兼容性问题)，不好配置，经常配置失败
2、2021年的自动化课程邮件发送，unittestreport来发送邮件
   1、构造邮件：标题，正文，附件，发送给谁，谁发送，协议
   2、执行完测试用例，会生成一个html文件，就用作邮件的附件
   3、发送邮件

"""


import unittest
from unittestreport import TestRunner

#创建测试套件：用来收集测试用例
su = unittest.defaultTestLoader.discover(start_dir=".", pattern='demo*.py')

runner = TestRunner(
                 suite=su,
                 filename="py52report.html",
                 report_dir="./reports",
                 title='接口测试报告',
                 tester='海励',
                 desc="上课项目测试生成的报告",
                 templates=2
                    )

runner.run()
runner.send_email(host="smtp.qq.com",
                  port=465, #163 端口是 25   qq邮箱465
                  user="1605118090@qq.com",
                  password="oyukpnrnjirebahb",
                  to_addrs=["1605118090@qq.com","228628874@qq.com",
                              "1942595902@qq.com","1954429849@qq.com",
                              "2046804899@qq.com","184011435@qq.com"],
                    )


