"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/6/22 20:57
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
增删改查
字符串(str)
一、特性
1、字符串是不可变的数据类型
    test_str = "python52"
    print(id(test_str))
    print(test_str)
    
    test_str = "hello"
    print(id(test_str))
    print(test_str)
2、有序的：可以通过索引取值，索引从0开始
3、可迭代：可以通过循环去获取他的值

二、访问字符串
# test_str = "p      y       t     h       o     n    5     2"
#            #0      1       2     3       4     5    6     7
#            #-8    -7      -6     -5     -4    -3   -2    -1

1、通过正序索引取值：从0开始
result = test_str[4]
2、倒序索引取值：从-1开始
result2 = test_str[-7]
3、通过值获取索引
result3 = test_str.index("h")
4、获取字符串的长度
len(test_str)
5、字符串切片
test_str[start_index:stop_index:step]
1、正序切片步长可以不写，默认是1
2、切片遵循左闭右开原则(包含起始索引的值，不包含结束索引的值) 
3、起始索引不写，默认从0开始
4、结束索引不写，默认为字符串的长度
5、正序切片用正序索引，倒序切片用倒序索引
6、步长，正序切片可以不写，倒序切片一定要写，因为步长前面的符号表示正序还是倒序
7、倒序切片，起始索引不写默认索引从-1开始，结束索引不写，默认到字符串的长度

三、操作
1、成员运算,返回布尔值
in: 是某某的成员
not in ： 不是某某的成员

"""

test_str = "python52"
print("h" not in test_str)

# {}  []  ()
#test_str[start_index:stop_index:step]

#正序切片
# result = test_str[2:6:1]
# print(result)

#倒序切片，不用【面试可能用到】
#不准这样切片
# result = test_str[-6:-2:1]

# 倒序切片
# result = test_str[-1:-6:-2]
# print(result)

#倒序索引妙用 ==字符串反转
result = test_str[::-1]
print(result)

# test_str = "p      y       t     h       o     n    5     2"
#            #0      1       2     3       4     5    6     7
#            #-8    -7      -6     -5     -4    -3   -2    -1




# test_str = "python52"
#正序索引从0开始
# result = test_str[4]
# print(result)

# 倒序索引从-1开始
# result2 = test_str[-7]
# print(result2)
# result3 = test_str.index("h")
# print(result3)


#获取长度
# print(len(test_str))


#不可变类型
# test_str = "python52"  id   === test_str
# print(id(test_str))    输出：python52
# print(test_str)
# test_str = "hello"      id === test_str
# print(id(test_str))
# print(test_str)         输出：hello
# test_str = "python52"