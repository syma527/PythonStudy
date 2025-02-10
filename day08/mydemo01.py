"""
for while
一、range函数
作用：用于生成一个可迭代对象
语法：range（起始索引值，结束索引值，步长）
二、循环控制关键字
1、continue：结束本次循环，进入下一轮循环
for i in range（10）

"""
# 二、循环控制关键字
"""
for i in range(10):
    if i == 5:
        continue
    print(i)
print('\n')
for i in range(10):
    if i == 5:
        break
    print(i)
"""
"""
三、for循环和while 循环的使用场景
1、知道循环次数的时候用for循环
2、不知道循环次数的时候用while循环

import random
num = 0
while num < 10:
    print('num的值',num)
    n = random.randint(1,10)
    print("随机生成数", n)
    num += n

for i in range(10):
    if i == 5:
        continue
    print(i)
"""
# 起始索引值，结束索引值，步长
# for i in range(1,6,2):
#     print(i)
# print("="*20)

# str = "123456"
# print(str[1:5:2])

# for i in (1,2,3,4,5,7):
#     print(i)
# test_list = ['a','b','c','d',2]
# for i in test_list:
#     print(i)
"""
test_list = ['a','b','c','d',2]
print("="*20)
for index in range(4):
    print(test_list[index])
"""
"""
for i in range(1, 10):
    for k in range(1, i + 1):
        print("{} * {} = {} \t".format(k, i, k * i),end="")
    print()
"""

# for index in range(4):
#     print(test_list[index])
# print()
# import random
# num = 0
# while num < 10:
#     print("num的值",num)
#     n = random.randint(1,10)
#     print("随机生成数", n)
#     num += n
"""
test_list = [1, 2, 3, 4, 5, 6]
for i in test_list:
    print(i)

print("=" * 20)
for index in range(6):
    print(test_list[index])
print(list(range(6)))

test_list = [1, 2, 3, 4, 5, 6]
for i in range(-1, -6, -1):
    print(test_list[i])

n = 0
while n < 10:
    print("外层循环的值", n)
    num = 0
    while num < 5:
        print("内层循环的值：", num)
        num += 1
    n += 3

for i in range(3):
    print("外层循环的值:", i)
    for j in range(3):
        print("内层循环的值：", j)

def add(x,y):
    print("x的值:", x)
    print("y的值:", y)
    return x + y
res = add(y = 9, x = 10)
print(res)

def sum_num(name, age, *args, **kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)

sum_num("laowang",40,40,50,first_name = "花鼓")


def add(**kwargs):
    return kwargs
test_dict = {"name":"zhangsan", "age": "30"}
result = add(**test_dict)
print(result)
"""
def add(x = 1, y = 1):
    print("x的值", x)
    print("y的值", y)
    return x + y
result = add(x = 6,y = 4)
print(result)
