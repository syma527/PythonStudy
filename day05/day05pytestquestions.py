"""
#第一题 创建一个包含1到10的整数列表，然后打印这个列表。
list_01 = [0,1,2,3,4,5,6,7,8,9,10]
print(list_01)
# 第二题 给定列表 fruits = ["apple", "banana", "cherry", "date"]，分别用正索引和负索引访问并打印 "cherry"。
fruits = ["apple",'banana',"cherry","date"]
print(fruits[2])
print(fruits[-2])


# 第三题 给定列表 numbers = [10, 20, 30, 40, 50]，使用切片取出中间三个元素（20, 30, 40）。
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])


# 第四题将列表 colors = ["red", "green", "blue"] 修改为 ["red", "yellow", "blue", "purple"]（替换green为yellow并在末尾添加purple）
colors = ["red", "green", "blue"]
colors.insert(1,"yellow")
colors.remove("green")
colors.append("purple")
print(colors)


# 第五题 给定列表 scores = [85, 92, 78, 96, 88]，在列表开头插入分数70。
scores = [85, 92, 78, 96, 88]
scores.insert(0,70)
print(scores)


# 第六题 从列表 animals = ["cat", "dog", "rabbit", "hamster", "bird"] 中删除 "rabbit"（使用两种不同方法各做一次）

animals = ["cat", "dog", "rabbit", "hamster", "bird"]

# animals.pop(2)
print(animals)
animals.remove('rabbit')
print(animals)

#  第7题 使用 append() 和 extend() 分别向空列表 my_list = [] 添加元素，使最终结果为 [1, 2, 3, 4, 5]（两种方式都要演示）

my_list = []

# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
# my_list.append(4)
# my_list.append(5)
# my_list.append(6)
# print(my_list)

my_list2 = [1,2,3,4,5]
my_list.extend(my_list2)
print(my_list)



# 第八题 给定列表 data = [3, 1, 4, 1, 5, 9, 2]，使用 sort() 和 sorted() 分别对它进行升序排序，并说明两者的区别

data = [3,1,4,1,5,9,2]
data.sort(reverse=False)
print(data)

data1 = [3,1,4,1,5,9,2]
my_data = sorted(data1)
print(my_data)
print(data1)

# sort 是直接在原来的list上做排序，sorted 可以作用在其他排序


# 第九题 使用列表方法统计列表 letters = ["a", "b", "c", "a", "d", "a", "b"] 中字母 "a" 出现的次数

letters = ["a", "b", "c", "a", "d", "a", "b"]
my_count = letters.count('a')
print(my_count)


# 第十题 使用 remove()、pop() 和 del 三种方式分别从列表 nums = [10, 20, 30, 40, 50] 中删除元素30，并打印每次删除后的列表
# nums = [10, 20, 30, 40, 50]

# nums.remove(30)
# print(nums)

# nums.pop(2)
# print(nums)
# del nums[2]
# print(nums)
#  第11题 编写代码将列表 mixed = [1, "hello", 3.14, True, "world"] 中的所有字符串元素提取出来，组成一个新列表

mixed = [1, "hello", 3.14, True, "world"]

strings = [item for item in mixed if isinstance(item,int)]
print(strings)

# 第12题 使用列表推导式创建一个包含1到20中所有偶数的列表
int_list = [x  for x in range(1,21) if x % 2 == 0 ]
print(int_list)

#第13题? 使用嵌套列表推导式生成一个3×3的乘法表列表，例如：[[1, 2, 3], [2, 4, 6], [3, 6, 9]

list1 = []
list2 = [[ i * j for i in range(1,4)] for j in range(1,4)]
print(list2)


#第14题 看ai 给定二维列表 matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]，分别打印主对角线元素（1,5,9）和次对角线元素（3,5,7）
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(tuple(matrix[i][3-1-i] for i in range(3)))

#第15题  将一个字符串 "Python is awesome" 按空格分割成单词列表，然后将每个单词首字母大写后重新组成新列表
str_change = "Python is awesome"
str_02 = str_change.split()
str_03 = []
for i in list(str_02):
    str_03.append(i.title())

print(str_03)


#第16题 编写一个函数 remove_duplicates(lst)，接受一个列表参数，返回一个去除重复元素后的新列表（保持原有顺序）
def remove_duplicates(lst):
    seen = set()
    res = []
    for x in lst:
        if x not in seen:
            res.append(x)
            seen.add(x)
    return res
if __name__ == '__main__':
    li_1 = [22,3,4,3,5]
    print(remove_duplicates(li_1))


# 17题给定两个等长列表 names = ["Alice", "Bob", "Charlie"] 和 ages = [25, 30, 35]，使用 zip() 将它们合并成一个字典，然后再转回成嵌套列表形式 [["Alice", 25], ["Bob", 30], ...]。

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

res = [[n,a] for n,a in zip(names,ages)]
print(res)


#第18题 实现一个简单的购物车程序：用列表存储商品名称，用户可以反复输入商品名加入购物车，输入"quit"退出，最后打印购物车所有商品及总数

list_product = []
while True:
    res = input("请输入商品名称")
    if res != "quit":
        list_product.append(res)

    else:
        break

print("商品名称",list_product)
print("总数",len(list_product))


"""


