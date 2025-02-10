"""
1.通过键值对表示元素
2、key不能重复，如果重复会被覆盖掉
3、key不能是容器数据类型
"""
"""
test_dict = {'host': '192.168.1.1', 'port': '33061', 'user': 'root', 'pwd': 'test123'}
print(test_dict)
# 通过关键字dict和二元组列表创建
# res_dict = dict([('host', '142.155.1.2'), ('port', '4456'),('user', 'root'),('pwd', 'test2334')])
# print(res_dict)
test_dict = {'host': '192.168.3.1', 'port': '33061', 'user': 'root', 'pwd': 'sdfsafd12'}
# 通过key去访问
host = test_dict['host']
print(host)
# 2、get获取不存在的key 不会报错，会返回默认值
res = test_dict.get('host1', 'test')
print(res)
# 获取所有的key，返回的数据类型为keys，不能直接获取元素，需要进行数据类型转换
res_allkey = test_dict.keys()
print(res_allkey)
res_allvalues = test_dict.values()
print(res_allvalues)
# 5、获取所有的key，value，返回的数据类型为 dict_items,不能直接获取元素，需要进行数据类型转化
res_allitems = test_dict.items()
print(res_allitems)
for val in test_dict.values():
    print(val)
for key, val in test_dict.items():
    print(key, val)
# 修改
# 1、通过key修改值
# key存在，修改key对应的value
test_dict['host'] = '192.168.1.22'
res_key = test_dict['host']
print(res_key)
print(test_dict)
test_dict.setdefault('db','lemon_test')
print(test_dict)
test_dict.setdefault('db','lemon_test234')
print(test_dict)
# 合并字典

# test_dict1 = {'host': '192.168.1.2', 'port': '3454', 'user': 'test_user'}
# test_dict2 = {'user': 'root', 'pwd': 'test234'}
# test_dict1.update(test_dict2)
# print(test_dict1)

test_dict = {'host': '192.168.2.1', 'port': '34534', 'user': 'root', 'pwd': 'sdfasd'}
del test_dict['host']
print(test_dict)
test_dict['host'] = '165.2.3.45'
print(test_dict)
res_delete = test_dict.pop('port')
print(res_delete)
print(test_dict)

res = test_dict.values()
print(res, type(res))
print(list(res)[0])

test_dict = {'host': '192.168.2.1', 'port': '34534', 'user': 'root', 'pwd': 'sdfasd'}
res = test_dict.items()
print(res,type(res))
"""
test_dict = {'host': '192.168.1.1', 'port': '2323', 'user': 'admin', 'pwd': 'test123'}
# print(test_dict)
host = test_dict['pwd']
# print(host)

res = test_dict.items()
# for val in test_dict.keys():
#     print(val,'\t', end="")

# for val in test_dict.values():
#     print(val,'\t',end = "")

del test_dict["port"]
print(test_dict)



res2 = test_dict.popitem()
print(res2)

