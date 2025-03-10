"""
============================
Project: py52Api
Author:柠檬班-海励
Time:2022/9/26 21:29
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
import pytest
import unittest
from ddt import data, ddt

from tools.handle_excel import HandleExcel
from tools.handle_path import case_data_dir

from tools.handle_replace import HandleReplace
from tools.handle_response import HandleResponse
from tools.handle_extract_data import HandleExtractData
from tools.handle_request import HandleRequest
from tools.handle_mysql import mysql
from tools.handle_assert_db import HandleAssertDb
from tools.handle_setup_sql import HandleSetupSql


# 从excel中拿到login页的测试数据
case_list = HandleExcel(file_name=case_data_dir, sheet_name="place_order").get_cases()

@pytest.fixture(scope="class")
def init_class():
    replace = HandleReplace()
    response = HandleResponse()
    extract = HandleExtractData()
    request = HandleRequest()
    assert_db = HandleAssertDb()
    setup_sql = HandleSetupSql()
    yield replace,response,extract,request,assert_db,setup_sql
    mysql.close_db()

@pytest.mark.usefixtures("init_class")
class TestPlaceOrder:
    @pytest.mark.parametrize("case",case_list)
    def test_place_order(self, case,init_class):
        replace,response,extract,request,assert_db,setup_sql = init_class
        #执行前置sql语句
        setup_sql.setup_sql(sql_list=case["setup_sql"])
        #替换请求参数
        data = replace.replace_data(data=case["data"])
        print("请求参数的数据类型:", type(data))
        #发请求
        response = request.send_request(is_upload=case["is_upload"],url=case["url"],method=case["method"],data=data,port=case["port"])
        #接口断言
        response.assert_responsee(response=response, expected_data=case["expected_data"])
        #提取数据，设置为类属性
        extract.extract_data(response=response,extract_data=case["extract_data"])
        #数据库断言
        assert_db.assert_db(assert_db=case["assert_db"])
