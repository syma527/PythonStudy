"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/1 20:42
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
数据类型转换
一、能直接相互转换(样子不会变化)
1、int <==> str
2、list <==> tuple
3、list <==> set
4、tuple <==> set
list <==> tuple <==> set 3个类型可以互相转换，当转换成set时，重复的值，会被去重

二、不能直接相互转换(样子是会变化的)
1、str ==> tuple
2、str ==> list
3、str ==> set


"""

test_str = "python"
test_str = list(test_str)
print(test_str)
new_str = ''.join(test_str)
print(type(new_str))

test_str = "python"
test_str = tuple(test_str)
print(test_str)
new_str = ''.join(test_str)
print(type(new_str))


test_str = "python"
test_str = set(test_str)
print(test_str)
new_str = ''.join(test_str)
print(type(new_str))

"""
# tuple == set
test_list = ('a','b','c','c')
print(test_list)
print(type(test_list))

test_list = set(test_list)
print(test_list)
print(type(test_list))

test_list = tuple(test_list)
print(test_list)
print(type(test_list))


# list == set
test_list = ['a','b','c']
print(test_list)
print(type(test_list))

test_list = set(test_list)
print(test_list)
print(type(test_list))

test_list = list(test_list)
print(test_list)
print(type(test_list))


# list == tuple
test_list = ['a','b','c']
print(test_list)
print(type(test_list))

test_list = tuple(test_list)
print(test_list)
print(type(test_list))

test_list = list(test_list)
print(test_list)
print(type(test_list))




# int == str
num_str = 100
print(num_str)
print(type(num_str))

num_str = str(num_str)
print(num_str)
print(type(num_str))

num_str = int(num_str)
print(num_str)
print(type(num_str))


"""



