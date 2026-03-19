"""list_001 = [1,3,4,5]
t_002 = 34
# list_001.append(t_002)
# print(list_001)
list_001.extend(t_002)
print(list_001)




nums = [1,3,5,6,4,54]

nums[4:4] = [-1,-2,-3]

print(nums) # 对空切片,直接在下标为4的后面,插入整串字符,




list1 = ['tom','lucy','wilia']

name = input('需要的查找的名字是')


if name in list1:
    print('找到了')

else:
    print('找不到')


nums = [1,2,4,5,6,6,8,2,2,'willa','tom','willa']
print(nums.count('willa'))

li1 = [1,3,4,5,'张三']

print('原列表',li1)

li1.reverse()
print('倒置后',li1)

"""

li = [1, 34, 4, 5, 5, 67, 7, 6, 5, 9]
li2 = []

i = 0

while i < len(li) + 1:
    if i in li:
        li2.append(i * 2)

    i += 1
print(li2)
