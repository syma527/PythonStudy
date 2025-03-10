"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/8/5 21:50
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""

一、为什么要做数据提取
1、接口之间又数据依赖，鉴权的token
二、数据提取的方式
1、针对json数据：jsonpath
2、针对字符串数据：re

三、python如何处理json
import json
python_dict = {"key1":"val1","key2":None,"key3":True,"key4":False}
#将dict转换成jsonstr
result = json.dumps(python_dict)
print(result)
#将jsonstr转换成dict
res2 = json.loads(result)
print(res2)


"""
# java_dict = {"key1":"val1","key2":null,"key3":true}

import json
python_dict = {"key1":"val1","key2":None,"key3":True,"key4":False}
#将dict转换成jsonstr
result = json.dumps(python_dict)
print(result)
#将jsonstr转换成dict
res2 = json.loads(result)
print(res2)


resp = {"resp":[{'access_token': 'b614638c-aa25-4ef7-a54a-7775aab55de2',
 'token_type': 'bearer',
 'refresh_token': '8713a350-c2f0-44b8-83a3-7ca373d922ed',
 'expires_in': 1295999},"demo"]}
token = resp["resp"][0]["access_token"] #字典取值
