"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/6 20:30
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
三、内置函数
1、print()
2、input()
3、数据类型：int  str   list   tuple   set  dict  
4、type  
5、isinstance
6、id
7、sort
8、sorted
9、计算相关：sum   max   min    len   count
10、range
11、random

四、高阶函数
博客地址：
http://testingpai.com/article/1617365033112
1、zip【掌握】
作用：打包函数
如果两个list元素个数不一样，打包成字典的时候以元素个数较少的为准去创建字典
l1 = ['a','b','c','d']
l2 = [1,2,3]
res = dict(list(zip(l1,l2)))
print(res)

l1 = ['a','b','c']
l2 = [1,2,3,4]
#在原来的基础上解压，没打包成字典
# res = list(zip(l1,l2))
# print(res) #list嵌套[('a', 1), ('b', 2), ('c', 3)]
# result = list(zip(*res))
# print(result)

# 打包成字典
#dict([('a', 1), ('b', 2), ('c', 3)])
result  = dict(list(zip(l1,l2)))
print(result)
# 解压
# print(list(result.items()))
test_list = list(result.items())
print("这里是字典的key和value组成的元组放在list中：",test_list)
res2 = list(zip(*test_list))
print(res2)


2、lambda：匿名函数
语法： func = lambda 函数的参数:返回值
def test01(x,y):
    return x+y

#lambda 函数的参数:返回值
func = lambda x,y:x+y
result = func(1,5)
print(result)

test_list = [[1,33,4],[2,22,6],[5,55,1]]
test_list.sort(key=lambda x : x[1])
print(test_list)

# [(key1,val1),(key4,val5),(key3,val6)]
test_dict = {"key1":"val1","key4":"val5","key3":"val6"}
result = sorted(test_dict.items(),key=lambda x:x[0])
print(dict(result))


3、enumerate
test_list = ['a','b','c']
result = dict(list(enumerate(test_list)))
new_dict = {}
for key,val in result.items():
    print(key,val)
    new_dict[val]=key
print(new_dict)
#设置生成的索引值从1开始
res = list(enumerate(test_list,1))
print(res)

4、map()
作用：将一个可迭代对象的数据，传入一个函数进行遍历操作
传统用法
def test01(x):
    return x*2
result = map(test01,[1,2,3])
print(list(result))

#结合lambda使用
result = list(map(lambda x:x*2,[1,2,3] ))
print(result)

本质：
new_list = []
for i in [1,2,3]:
    result = test01(x=i)
    new_list.append(result)
print(new_list)

"""

# 传统用法
# def test01(x):
#     return x*2
# result = map(test01,[1,2,3])
# print(list(result))


# new_list = []
# for i in [1,2,3]:
#     result = test01(x=i)
#     new_list.append(result)
# print(new_list)


# 结合lambda使用
# result = list(map(lambda x:x*2,[1,2,3] ))
# print(result)
"""
test_dict = {"key1": "val1", "key2": "val2", "key3": "val4"}
result = sorted(test_dict.items(), key=lambda x: x[0])
print(dict(result))

new_dict = {}
for key, val in result.items():
    print(key, val)
    new_dict[val] = key

print(new_dict)
# 设置生成的索引值从1开始
# res = list(enumerate(test_list, 1))
# print(res)

"""


def test01(x):
    return x * 2


result = map(test01, ['a', 'b', 'c'])
print(list(result))
result = list(map(lambda x: x * 2, [1, 2, 3]))
print(result)

new_list = []
for i in [1, 3, 3]:
    result = test01(x=i)
    new_list.append(result)
print(new_list)
