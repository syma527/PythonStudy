"""
1.print()
2.input()
3.int str list tuple set dict
4.type
5.isinstance()
6.id
7.sort  //
8.sorted
9.sum max min len count
10. range
11.random


zip
如果两个list元素个数不一样，打包成字典的时候以元素个数较少的为准去创建字典
l1 = ['a', 'b', 'c', 'd']
l2 = [1, 2, 3, 4]
res = dict(list(zip(l1, l2)))
print(res)

l1 = ['a', 'b', 'c']
l2 = [1, 2, 3, 4]
res = list(zip(l1,l2))
print(res)
result = list(zip(*res))
ll1 = list(result[0])
ll2 = list(result[1])
print(ll1)
print(ll2)

l1 = ['a', 'b', 'c']
l2 = [1, 2, 3, 4]
dict([('a', 1), ('b', 2), ('c', 3)])
result = dict(list(zip(l1, l2)))
print(result)


def test01(x,y):
    return x + y
# lambda 函数的参数：返回值
func = lambda x,y:x + y
result = func(1,5)
print(result)

func = lambda x, y: x + y
result = func(1, 5)
print(result)
test_list = [[1, 22, 4], [2, 55, 4], [4, 67, 4]]
test_list.sort(key=lambda x: x[1])
print(test_list)


# [(key1,val1),(key2,val2),(key3,val3)]
test_dict = {"key1": "val1", "key2": "val2", "key3": "val4"}
result = sorted(test_dict.items(), key=lambda x: x[0])
print(dict(result))



# 循环遍历 将一个可迭代对象的数据，传入一个函数进行遍历操作
def test01(x):
    return x * 2


result = map(test01, [1, 2, 3])
print(list(result))
"""

# def test01(x):
#     return x * 2
#
#
# new_list = []
# for i in [1, 2, 3]:
#     result = test01(x=i)
#     new_list.append(result)
# print(new_list)

"""
四、基本概念
模块： 在python里面的py文件就叫模块
目录：目录就是普通的目录（文件夹）
包： 有__init__.py文件的目录就叫包

包用来管理模块的

五、模块导入
1、python自带的包或者模块
2、第三方包（库）
3、自定义包（模块）

六、包管理
1、pip 用来管理第三方的包，解决安装包相互依赖的问题
pip list 查看已安装

l1 = ['a', 'b', 'c']
l2 = [1, 2, 3, 4]
res = list(zip(l1, l2))
print(res)
result = list(zip(*res))
print(list(result[0]))
print(list(result[1]))

l1 = ['a', 'b', 'c']
l2 = [1, 2, 3, 4]
result = dict(zip(l1, l2))
print(result)
print(list(result.items()))
test_list = list(result.items())
print(test_list)
res2 = list(zip(*list(result.items())))
print(res2[0])
print(res2[1])


func = lambda  x,y: x+y
result = func(1,5)
print(result)
"""
test_list = [[1, 33, 4], [2, 45, 6], [3, 65, 3]]
test_list.sort(key=lambda x: x[1])
print(test_list)
test_set = {1, 2, 3, 43, 3, 4, 4, 45, 5, 6, 7, 8, 8, 7, 8, 9, 0, 0, 2, 2, 'a', 'c', 'd'}
print(test_set)
for i in test_set:
    print(i + \t, end='')
