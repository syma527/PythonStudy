"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/8/8 20:07
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

四、jsonpath用法
1、安装jsonpath
pip install jsonpath==0.82

2、使用语法(表达式)，返回的结果放在list中
总结：json里面如果是字典就用.name或者[name]来取值,如果是list(元组)可以用索引取值(不支持倒序索引)
1、$ 表示根元素
"$.lemon"
2、. 和[] 表示子元素
"$[lemon]"
"$.java"
"$[lemon].java.name"
3、.. 表示递归搜索，从根元素开始去搜索[掌握]
"$..name"
4、[]切片操作，子元素操作
"$..python.[1,3]  索引取值
"$..python.[1:3]  切片(和list的切片一致)

5、获取子元素的某个属性
"$..python.[1:3].[name,age]"
6、?() 过滤表达式
"$..python.[?(@.height > 185)]"
7、成员运算(in、not in)
"$..python.[?(@.name not in ['心蓝','木森'])]"
8、逻辑运算
"$..python.[?(@.height >= 185 and @.age > 26 )]"
"$..python.[?(@.height >= 185 or @.age < 26 )]"
"""


from jsonpath import jsonpath

teacher_info = {
    "name":"柠檬班",
    "lemon":
    {
    "python": [
        {"name": "海励",
         "sex": "男",
         "age": 30,
         "height": 175,
         "info":"python自动化老师"
         },
        {"name": "木森",
         "sex": "男",
         "age": 26,
         "height": 185,
         "info":"python测开老师"
         },
        {"name": "小简",
         "sex": "女",
         "age": 18,
         "height": 170,
         "info":"python自动化老师"
         },
         {"name": "心蓝",
         "sex": "男",
         "age": 28,
         "height": 185,
          "info":"python测开老师"
         },
         {"name": "雨泽",
         "sex": "男",
         "age": 28,
         "height": 190,
         "info":"python自动化老师"
         }
    ],
    "java": {
        "name": "三宝",
        "sex": "男",
        "age": 30,
        "height": 185.5,
        "info":"java测开老师"
    }
}
}
# .  []
# list
# 总结：json里面如果是字典就用.name或者[name]来取值,如果是list(元组)可以用索引取值

# res = jsonpath(teacher_info,"$.name")
# res = jsonpath(teacher_info,"$[lemon].java.name")
# res = jsonpath(teacher_info,"$..name")[-1]
# res = jsonpath(teacher_info,"$..python.[1,3]")
# res = jsonpath(teacher_info,"$..python.[1:3]")
# res = jsonpath(teacher_info,"$..python.[1:3].[name,age]")
# res = jsonpath(teacher_info,"$..python.[?(@.height > 185)]")

#成员运算

# res = jsonpath(teacher_info,"$..python.[?(@.name not in ['心蓝','木森'])]")

# 逻辑运算
# res = jsonpath(teacher_info,"$..python.[?(@.height >= 185 && @.age > 26 )]")
# res = jsonpath(teacher_info,"$..python.[?(@.height >= 185 or @.age < 26 )].[name,age]")


res = jsonpath(teacher_info,"$..name")
print(res)




resp = {"access_token":"3663846c-e626-4a03-af44-d160c7cc2082","token_type":"bearer","refresh_token":"740212d4-d52e-4e25-8e33-5ce9cf5a2581","expires_in":1295999}
res2 = jsonpath(resp,"$..access_token")[0]
print(res2)



