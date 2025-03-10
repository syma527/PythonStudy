"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/1 21:10
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
控制流

一、流程
流程概念：做一件事情的先后顺序
        学习流程：上课听懂 --- 课后回放+做笔记 --- 写作业
流程分类：顺序结构、选择结构、循环结构


二、顺序结构
1、代码从上往下执行

三、选择结构(只会执行一个语句体)
1、单if语句
num = 100
if num == 10:
    print("num 为 100")
2、标准的if--else语句
num = 100
if num == 100:
    print("num 为 100")
else:
    print("num 不等于10")

3、复合if--elif---else语句
num = 10
if num == 10:
    print("num 等于 10")
elif num > 10:
    print("num 大于10")
elif num == 20:
    print("num 等于 20")
else:
    print("num 小于10")


四、循环结构
1、可迭代对象
   1、能够通过for循环取值的数据类型
   2、判断是否是可迭代对象，返回布尔值
    test_str = "python"
    from collections.abc import Iterable
    result = isinstance(test_str,Iterable)
    print(result)
    
2、for 循环
   1、可以遍历字符串、列表、元组、字典、集合

3、while循环(一定要记得设置退出条件，不设置退出条件就是死循环)
   num = 0
   while num < 10:
        print(f"num = {num}")
        num += 1

"""










num = 0
while num < 10:
    print(f"num = {num}")
    num += 1
    num += 1
    num += 1
    num += 1
    num += 1




"""



#单if语句
num = 100
if num == 10:
    print("num 为 100")

#标准的if--else语句
num = 100
if num == 100:
    print("num 为 100")
else:
    print("num 不等于10")
print(f"num 的值：{num}")

#标准的if--else语句
num = 10
if num == 10:
    print("num 等于 10")
elif num > 10:
    print("num 大于10")
elif num == 20:
    print("num 等于 20")
else:
    print("num 小于10")
    
    
    
test_str = "python"
test_list = {'a','b','c'}
for i in test_list:
    print(i)
test_dict = {"key1":"val1","key2":"val2"}
#遍历key，默认是遍历key
for val in test_dict:
    print(val)
#遍历key
for val in test_dict.keys():
    print(val)
#遍历value
for val in test_dict.values():
    print(val)
#遍历key和value
for key,val in test_dict.items():
    print(key,val)
"""




