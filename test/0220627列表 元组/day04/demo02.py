"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/6/24 21:34
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
字符串格式化【掌握】
一、%占位符【了解】
1、%s：表示字符串占位，接收字符串类型的数据，如果是数值，会强制转换成字符串类型
test_str = "%s say today is nice day %s" %("老王","1111")
2、%d：表示数值占位，接收数值类型，只能是Int类型，如果传float会抹掉小数点后的值
test_str = "%s  price is %d" %("iphone 13 ",123.999)
3、%f：表示浮点数据占位，不设置小数位数默认精确到小数点后6位
test_str = "%s  price is %f" %("iphone 13 ",123.999)
test_str = "%s  price is %.2f" %("iphone 13 ",123.999)
test_str = "%s  price is %.2f" %("iphone 13 ",123)

二、format
1、按顺序取值
test_str = "{}  price is {}".format("iphone13",123.02)
2、按索引取值
test_str = "{1}  price is {0}".format("iphone13",123.02)
test_str = "{1}  price is {0} and {1}".format("iphone13",123.02)
3、按关键字取值
test_str = "{name}  price is {price} and {price}".format(name="iphone13",price=123.02)

三、f表达式
name="iphone13"
price = 10
num = 10
test_str = f"{name}  price is {price} and {price+num}"

"""
name="iphone13"
price = 10
num = 10
test_str = f"{name}  price is {price} and {price+num}"
print(test_str)
# insert into table(shop_id,name,key1)value({name},{key},{test})









# test_str = "%s say today is nice day %s" %("老王","1111")
# print(test_str)

# test_str = "%s  price is %d" %("iphone 13 ",123.999)
# print(test_str)


# test_str = "%s  price is %f" %("iphone 13 ",123.999)
# test_str = "%s  price is %.2f" %("iphone 13 ",123)
# print(test_str)





