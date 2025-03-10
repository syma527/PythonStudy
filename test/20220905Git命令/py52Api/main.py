"""
============================
Project: py52Api
Author:柠檬班-海励
Time:2022/8/12 20:54
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""

import unittest,unittestreport
from tools.handle_path import case_dir,file_name,report_dir


suite = unittest.defaultTestLoader.discover(start_dir=case_dir,pattern="test_6_place_order.py")
runner = unittestreport.TestRunner(
                 suite=suite,
                 filename=f"{file_name}.html",
                 report_dir=report_dir,
                 title='接口自动化测试报告',
                 tester='老柠檬',
                 desc="商城项目接口测试报告",
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



