"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/6/27 21:44
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
元组【做了解】

一、特性
1、元素可重复
2、可以通过索引获取
3、元组本身不可修改
4、当元组只有一个元素的时候要加一个逗号
5、元素的数据类型可以不一致



二、创建
test_tuple = (1,'a')
test_tuple = (1,)

三、查询
1、通过索引取值
test_tuple[1]
2、查询长度
len(test_tuple)
3、切片
同字符串和列表

四、可变与不可变
1、不可变：元组本身不支持修改
2、可变：元组里面嵌套了可变的数据类型(list)


五、支持各种嵌套
test_demo = [(),(),[],"python",123]
""  ''   """"""   ''''''
[]
()
{}
{"":""}

"""

test_tuple = (1,'a','b',1,22,[1,2,3])
print("元组的id=",id(test_tuple))

l1 = test_tuple[-1]
print("未修改的l1=",l1)
print("列表id = ",id(l1))
l1[0]=999

print(test_tuple)
print("修改后的li = ",l1)
print("列表id = ",id(l1))
print("元组的id=",id(test_tuple))


test_demo = [(),(),[],"",123]

# (1,'a','b',1,22,2048840913416)   2048840913416 ==  [1,2,3]
# (1, 'a', 'b', 1, 22, 2048840913416)  2048840913416 ==  [999, 2, 3]


# print(test_tuple)

# print(type(test_tuple))
# print(test_tuple[1])
# print(len(test_tuple))
# print(test_tuple)
# print(test_tuple[::-1])



