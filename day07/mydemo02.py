"""
一、能直接相互转换(样式不会变化)
int <==> str
"""
"""
str 转化成list 样式会变化 ，需要通过多一步转化才能转化
test_str = "python"
test_str = list(test_str)
print(test_str)
new_str = ''.join(test_str)
print(new_str)
print(type(new_str))

"""

"""
list 转换成tuple能直接转换
test_list = {1,2,3,4,5,6,7}
print(test_list)
test_list = tuple(test_list)
print(test_list)

"""
"""
list <==> set
test_list = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(test_list)
test_list = set(test_list)
print(test_list)
"""
"""
int <==>str 可以直接相互转换无变化
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
test_str = "python"
test_str = tuple(test_str)
print(test_str)
new_str = ''.join(test_str)
print(type(new_str))