"""
============================
Project: py52Api
Author:柠檬班-海励
Time:2022/9/2 21:23
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
import unittest
import unittestreport
import time

from test_cases.test_7_all import generator_case_class
from tools.handle_attribute import HandleAttr
from tools.handle_excel_all import HandleExcel
from tools.handle_path import case_data_dir
from tools.handle_path import case_dir,file_name,report_dir
from tools.handle_mysql import mysql
from tools.handle_move_file import HandleMoveFile

class Start:
    def __init__(self):
        self.excel = HandleExcel(file_name=case_data_dir)


    def __del_attribute(self):
        #HandleAttr.__dict__.keys() == list(vars(HandleAttr).keys())
        print("HandleAttr属性",HandleAttr.__dict__)
        attr_name = list(vars(HandleAttr).keys())
        for name in attr_name:
            if not name.startswith("_"):
                delattr(HandleAttr,name)
            else:
                print("下划线开头的私有属性不删除")

    def start(self):
        #将测试报告挪到history目录下去
        HandleMoveFile.move_file()
        #读取excel数据(通过sheet)
        sheetname_list = self.excel.wb.sheetnames
        for sheet_name in sheetname_list:
            #执行之前删除全局属性中自己设置的属性
            self.__del_attribute()
            #获取sheet的数据
            data_list =self.excel.get_cases(sheet_name=sheet_name)
            #用获取的数据去做数据驱动，动态生成测试用例
            case_class = generator_case_class(case_list=data_list)
            #收集测试用例
            suite = unittest.defaultTestLoader.loadTestsFromTestCase(case_class)
            #测试报告文件名称
            file_name = time.strftime("%Y%m%d_%H%M%S", time.localtime())
            #执行测试用例，生成测试，发邮件
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
                              port=465,  # 163 端口是 25   qq邮箱465
                              user="1605118090@qq.com",
                              password="oyukpnrnjirebahb",
                              to_addrs=["1605118090@qq.com", "228628874@qq.com",
                                        "1942595902@qq.com", "1954429849@qq.com",
                                        "2046804899@qq.com", "184011435@qq.com"],
                              )

        mysql.close_db()
        self.excel.wb.close()

if __name__ == '__main__':
    cl = Start()
    cl.start()



