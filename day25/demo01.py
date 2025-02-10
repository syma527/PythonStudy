"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/8/12 20:02
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、接口测试用例设计
接口地址、请求方式、请求头
1、有效等价类
{
  "t": 1660305852881,
  "principal": "student",
  "credentials": "123456a",
  "sessionUUID": "efb2f09c-e574-4c40-8a18-62ab6eebf6d9",
  "imageCode": "hhhh"
}

2、无效等价类
账号错误
{
  "t": 1660305852881,
  "principal": "student1111",
  "credentials": "123456a",
  "sessionUUID": "efb2f09c-e574-4c40-8a18-62ab6eebf6d9",
  "imageCode": "lemon"
}
密码错误
{
  "t": 1660305852881,
  "principal": "student",
  "credentials": "123456a1111",
  "sessionUUID": "efb2f09c-e574-4c40-8a18-62ab6eebf6d9",
  "imageCode": "lemon"
}
验证码错误
{
  "t": 1660305852881,
  "principal": "student",
  "credentials": "123456a1111",
  "sessionUUID": "efb2f09c-e574-4c40-8a18-62ab6eebf6d9",
  "imageCode": "lemon"
}
账号为空
{
  "t": 1660305852881,
  "principal": "",
  "credentials": "123456a",
  "sessionUUID": "efb2f09c-e574-4c40-8a18-62ab6eebf6d9",
  "imageCode": "lemon"
}
密码为空
{
  "t": 1660305852881,
  "principal": "student",
  "credentials": "",
  "sessionUUID": "efb2f09c-e574-4c40-8a18-62ab6eebf6d9",
  "imageCode": "lemon"
}
验证码为空
{
  "t": 1660305852881,
  "principal": "student",
  "credentials": "123456a",
  "sessionUUID": "efb2f09c-e574-4c40-8a18-62ab6eebf6d9",
  "imageCode": ""
}

测试用例设计方法：
等价类、边界值、流程分析、正交试验(因子+状态)、错误推断、因果图、状态迁移、探索测试

二、如何做好接口测试
功能测试：
1、了解业务(深度了解、某个功能怎么实现的、关联了哪些数据库表、实现逻辑)
2、会看接口文档
3、会抓包，会提取数据
4、会设计断言(用例设计)
5、数据库基本操作
自动化测试：
1、会代码尽量用代码来测试
2、数据库操作
3、框架设计(脚本设计)

三、项目框架模型
1、通用性：所有的接口走同一套逻辑
    1、参数替换
    2、发送接口请求
    3、接口响应断言
    4、提取全局变量的数据
    5、断言数据库
2、可扩展性+可维护性
3、分层设计+数据驱动
   数据层：excel管理测试数据
   工具类：读取excel的操作、发请求的操作、操作数据库的操作、日志收集、测试报告、数据替换、数据断言
   测试用例：unittest测试用例文件、业务逻辑
   配置文件：统一管理环境的配置数据
   框架入口：从某个文件开始执行你的框架
   
  
"""


def register(user,passwd):
    #在用户表把我的数据添加进去
    return {"cocde":"success"}







