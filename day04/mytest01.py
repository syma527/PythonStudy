# print(r"hello \n python")
# dir_path = "D:test.py"
# print(dir_path)
# dir_path = dir_path.upper()
# print(dir_path)
# dir_path = dir_path.lower()
# print(dir_path)
# dir_path = dir_path.swapcase()
# print(dir_path)
# dir_path = dir_path.title()
# print(dir_path)
# res = len(dir_path)
# print(res)
# res1 = dir_path.count("p")
# print(res1)
# dir_path_1 = "35304504"
# res2 = dir_path_1.isdigit()
# print(res2)
#
# res3 = (dir_path_1.split('3',-1))
# print(res3)
# test_str1 = "hello1"
# test_str2 = "python2"
# test_str = test_str1 +"\t\t"+ test_str2
# print(test_str)
#
# res = '_'.join(test_str1)
# res1 = test_str1 + test_str2
# print(res1)
#
# res = '_'.join(test_str1)
# print(res)

# test_str = "     www.lemon.com"
# res = test_str.replace("m","w")
# res1 = test_str.replace("n","2")
# print(res)
# print(res1)
#
# res3 = test_str.strip()
# print(res3)
# test_str = "%s say today is nice day %s" % ("老王", "11111")
# print(test_str)

# test_str = "%s price is %.2f" % ("iphone12",1223.222332333)
# print(test_str)

# test_str = "{} price is {}".format("iphone14",234)
# print(test_str)

# test_str = "{name} price is {price}".format(name= "zhangsan",price = "23423")
# print(test_str)

# test_str = "       www.lemon.com"
# res = test_str.strip()
# print(res)

# test_str = "python001"
# res = test_str[2]
# print(res)
#
# res2 = test_str[-1]
# print(res2)
# res3 = test_str.index("t")
# print(res3)
# res4 = len(test_str)
# print(res4)
#
# res5 = test_str[0:5:1]
# print(res5)
"""

特性
1、可变数据类型
2、有序（索引0开始）
3、元素可以重复
4、元素类型没有限制
5、可迭代

test_list = [2,3,45,6]
y = {'sdfsf','aaaa'}
test_set = {1, 4, 5, 7, 44, 66, 77, 88, 3, 45}
test_set.add('sas')
print(test_set)
test_set.update(y)
print(test_set)


num = 90
if num == 100:
    print("num 为 100")

else:
    print("num 不为 100")

from collections.abc import Iterable

test_str = ["sd",23,45]
result = isinstance(test_str,Iterable)
print(result)



num = 0
while num < 10:
    print("num = {num}",num)
    num += 1


test_str = "{1} price is {0}".format("iphone23",234.34)
print(test_str)



name = "iphone12"
price = 12
num = 32
test_str = f"{name} price is {price} and {num}"
print(test_str)

test_dict = {"sd":"sdf","sf":"345","dd":"456456"}
for val in test_dict.keys():
    print(val)



test_dict = {'host':"2323.2323","port":"2342342","usdf":"swerr3","pwd":"3234"}


res = test_dict.get("host",'test')


import operator

test_dict = {'host':"192.168.1.1","port":"32434","user":"root","pwd":"sasdf"}

def test(x):
    return x*2
t1 = test(100)
result = sorted(test_dict.items(),key = lambda x:x[0], reverse= True)
print(dict(result))
"""
numbers = [1,2,32,4,5,6,7,8]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(even_numbers)