"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/6/29 20:34
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、特性
1、通过键值对表示元素
2、key不能重复，如果重复了会被覆盖掉
3、key不能是容器数据类型

二、创建
1、test_dict = {'host':'192.168.1.1',"port":'33061',"user":"root","pwd":"test123"}
2、dict([('host', '192.168.1.1'), ('port', '33061'), ('user', 'root'), ('pwd', 'test123')])

三、查询
1、通过key去访问
test_dict = {'host':'192.168.1.1',"port":'33061',"user":"root","pwd":"test123"}
host = test_dict["host"]
2、get获取不存在的key不会报错，会返回设置的默认值
res = test_dict.get("host1","test")
3、获取所有的key，返回的数据类型为(<class 'dict_keys'>)，不能直接获取元素，需要进行数据类型转换
res = test_dict.keys()
4、获取所有的values，返回的数据类型为(<class 'dict_values'>)，不能直接获取元素，需要进行数据类型转换
res = test_dict.values()
5、获取所有的key，value，返回的数据类型为(<class 'dict_items'>)，不能直接获取元素，需要进行数据类型转换
res = test_dict.items()
6、for循环迭代
for val in test_dict.keys():
    print(val)
for val in test_dict.values():
    print(val)
for key,val in test_dict.items():
    print(key,val)
    
四、修改
1、通过key修改值
key存在，修改key对应的value
test_dict["host"] = "192.168.1.105"
key不存在，相当于添加一个键值对
test_dict["db"] = "lemon_test"

2、添加键值对
key不存在，就添加键值对
test_dict.setdefault("db","lemon_test")
key存在，什么都不做
test_dict.setdefault("host","lemon_test")

3、合并字典
test_dict1中key与test_dict2中的key重复，test_dict2中key对应的value会覆盖test_dict1中key对应的values
test_dict1 = {'host':'192.168.1.1',"port":'33061',"user":"test_user"}
test_dict2 = {"user":"root","pwd":"test123"}
test_dict1.update(test_dict2)

五、删除
test_dict = {'host':'192.168.1.1',"port":'33061',"user":"root","pwd":"test123"}
1、del test_dict["host"]
2、删除键值对，返回key对应的value
res = test_dict.pop("port")
3、删除最后一个进栈的
Python进出栈的原则：后进先出，测开内容
res2 = test_dict.popitem()
4、清空字典
test_dict.clear()

六、排序

脚本，自动化
1、容易错的地方(人工操作容易错、肉眼判断容易错)，用脚本或者自动化实现
2、繁琐的操作用自动化

"""
test_dict = {'host':'192.168.1.1',"port":'33061',"user":"root","pwd":"test123","db":"1212121212"}
del test_dict["host"]

res = test_dict.pop("port")
print(res)

# 删除最后一个进栈的
# Python进出栈的原则：后进先出
res2 = test_dict.popitem()
print(res2)

#清空字典
test_dict.clear()
print(test_dict)





# test_dict1 = {'host':'192.168.1.1',"port":'33061',"user":"test_user"}
# test_dict2 = {"user":"root","pwd":"test123"}
# test_dict1.update(test_dict2)
# print(test_dict1)
# print(test_dict2)



# test_dict = {'host':'192.168.1.1',"port":'33061',"user":"root","pwd":"test123"}
#key存在，修改key对应的value
# test_dict["host"] = "192.168.1.105"
# print(test_dict,id(test_dict))
# #key不存在，相当于添加一个键值对
# test_dict["db"] = "lemon_test"
# print(test_dict,id(test_dict))

#key不存在，就添加键值对
# test_dict.setdefault("db","lemon_test")
# print(test_dict)
# #key存在，什么都不做
# test_dict.setdefault("host","lemon_test")
# print(test_dict)





# test_dict = {'host':'192.168.1.1',"port":'33061',"user":"root","pwd":"test123"}
# test_dict1 = {"user":"root","port":'33061',"pwd":"test123",'host':'192.168.1.1'}
# print(test_dict == test_dict1) #比对值
# print(test_dict is test_dict1)  #比对id(内存地址)

# 如果key存在，修改key对应的value
# test_dict["host"] = "192.168.1.105"

#如果key不存在，相当于添加一个键值对
# test_dict["db"] = "lemon_test"
# print(test_dict)



#通过for循环迭代输出
# for val in test_dict.keys():
#     print(val)
# for val in test_dict.values():
#     print(val)
# for key,val in test_dict.items():
#     print(key,val)

#通过key获取对应的value
# host = test_dict["host"]


# get获取不存在的key不会报错，会返回设置的默认值
# 去通过host这个key去test_dict里面去找，是否存在，如果存在就返回host这个key对应的value
# 如果不存在，就返回你设置的值(test)
# res = test_dict.get("host","不存在的时候拿到的值放这里")
# print(res)


#获取所有的key
# res = test_dict.keys()
# print(res,type(res))
#转换数据类型才能获取值
# print(list(res)[0])


#获取所有的value

# res = test_dict.values()
# print(res,type(res))
# print(list(res)[0])


#获取所有的key和values
# res = test_dict.items()
# print(res,type(res))
# new_res = list(res)
# print(new_res,type(new_res))
# new_dict = dict(new_res)
# print(new_dict)


#变量赋值可以这么做,按顺序赋值
# key,val,val2 = 'host','192.168.1.1',100
# key = 'host'
# val = '192.168.1.1'
# val2 =  100
# print(key,val,)


"""
test_dict1 = {"key2":"val2"}
test_tuple = (1,2,3)
test_dict = {'key1':'val1',test_tuple:'bbb',"num":123,"test_list":[1,2,3]}
print(id(test_dict))
print(test_dict)

"""




