
# print(test_list)
#
# test_list[2] = "cccc"
# print(test_list)
#
# test_list.append('ddddd')
# print(test_list)
#
# test_list.insert(1,"xcc")
# print(test_list)
# l1 = [12,2,3,23,34]
# l2 = [3,3,4,34,45,56]
#
# l1.extend(l2)
# print(l1)
# print(l2)
test_list = [23,4,45,5,6,3,1,2,3,4,5,6]

# del test_list[-1]
# print(test_list)
# res = test_list.pop(-1)
# print(res)
# test_list.remove('a')
# print(test_list)

# print("b" in test_list)
# res = ord("h")
# print(res)
#
# test_list.sort()
# print(test_list)

"""
特性
元素可以重复
可以通过索引获取
元组本省不可被修改
当元组只有一个元素的时候要加一个逗号
元素的数据类型可以不一致
使用（）作为区分
常用在数据库中中使用，因为数据库中类型不能被修改
"""

test_tuple = (2,3,4,5,6,7,8,4,3,3,2)

# res = test_tuple[1]
# print(res)
#
# res_len = len(test_tuple)
# print(res_len)
# res_index = test_tuple.index(5)
# print(res_index)

test_tuple[2:11:1]
print(test_tuple)

test_tuple = (1,'a','b',2,44,[3,4,6])
# print("元组的id",id(test_tuple))
l1 = test_tuple[-1]
print("未修改的l1",l1)
print("列表id = ",id(l1))
l1[0] = 799

p