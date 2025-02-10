"""


test_list = ['a', 'b', 'c']
# 通过索引值访问
print(test_list[0])

test_list = ['a', 'b', 'c']
test_num = test_list.index('c')
print(test_num)



test_list = ['a', 'b', 'c', 3, 6, 89, 'sdfsd', '4omdfg']
test_len = len(test_list)
print(test_len)


test_ty = type(test_list)
print(test_ty)

test_list.append("changdong")
print(test_list)

"""
l1 = [1, 3, 4]

l2 = [2, 4, 6]

l2.extend(l1)
print(l1)
print(l2)

# 生成新的列表，不修改原有列表
l3 = l1 + l2
print(l3)

test_list = l3
print(test_list)
del test_list[-1]
print(test_list)
del test_list[0]
print(test_list)

res = test_list.pop(-1)
print(res)
print(test_list)