"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/6/27 19:58
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
列表[容器类型]
一、特性
1、可变数据类型(可修改)
2、有序(索引0开始)
3、元素可以重复
4、元素类型没有限制
5、可迭代

二、创建列表(增)
test_list = ['a','b','c']

三、访问(查询)
1、通过索引访问
test_list[0]
2、通过元素获取索引值
test_list.index("b")
3、查看列表的长度
len()
4、查看数据类型
type(obj)
5、切片
   1、切片同字符串
   2、倒序不一样

四、修改
1、通过索引修改值
test_list[0]="aaa"
2、添加新的元素
test_list.append("py52")
3、在某个位置(索引位置)插入元素
test_list.insert(1,'py52')
4、合并
将l2的元素通过追加的方式添加到l1
l1 = [1,2,3]
l2 = [4,5,6]
l2.extend(l1)
print(l1)
print(l2)

生成新的列表，不修改原有列表
l3 = l1+l2

五、删除
1、删除对应索引的值，无返回
del test_list[-1]
2、删除对应索引的值，返回被删除的元素
res = test_list.pop(-1)
3、删除元素(通过元素本身),删除找到的第一个匹配的值
test_list.remove(value)
4、清空list
test_list.clear()


六、其他操作
1、成员运算【返回布尔值】
   in ：存在，是某某的成员
   not in ： 不存在，不是某某的成员
test_list = ['a','b','c',1212,23,23,'a',['a','d',[1,2,3]]]
print('abbb' in test_list)


七、排序
原理：通过ascii码 大小排序
1、获取对应字符的ascii码
ord("h")
2、通过ascii码获取对应的字符
chr(104)

3、在原列表基础上排序
test_list.sort(reverse=True)
key: 用于嵌套列表排序，排序的依据
reverse: 默认是False升序，True:降序

4、排序后生成新的列表，不修改原来的列表
new_list = sorted(test_list,reverse=True)
key: 用于嵌套列表排序，排序的依据
reverse: 默认是False升序，True:降序



八、其他方法
1、求最值 
result = max(test_list)
result = min(test_list)
result = len(test_list)
result = sum(test_list)

九、拓展【学完for循环来看】
需求1-100求和
列表推导
print(sum([i for i in range(1,101)]))


"""














# print(ord("h"))
# print(chr(104))

# test_list = [23,2,45,6,34,89,23]
# result = max(test_list)
# result = min(test_list)
# result = len(test_list)
# result = sum(test_list)
# print(result)



# print(test_list,id(test_list))
#默认是升序
# test_list.sort(reverse=True)
# print(test_list)

#sorted不在原列表基础上排序，生成新的列表
# new_list = sorted(test_list,reverse=True)
# print(new_list,id(new_list))
# print(test_list,id(test_list))








# [[22,33],[1,43],[3434,5665]]





#泡泡堂   跑跑卡丁车  传奇   鬼泣

# test_list = ['a','b','c',1212,23,23,'a',['a','d',[1,2,3]]]
# print('abbb' in test_list)









#删除对应索引的值，无返回
# del test_list[-1]


#删除对应索引的值，返回被删除的元素
# res = test_list.pop(-1)
# print(res)
# print(test_list)


#删除元素(通过元素本身),删除找到的第一个匹配的值
# test_list.remove('a')
# test_list.remove('a')
# test_list[-1].remove('a')
# print(test_list)

#清空list
# test_list.clear()
# print(test_list)



#将l2的元素通过append的方式添加到l1
# l1 = [1,2,3]
# l2 = [4,5,6]
# l1.extend(l2)
# print(l1)
# print(l2)


# print(id(l1))
# l1 = l1+l2
# print(l1)
# print(l2)
# print(id(l1))


#生成新的列表，不修改原有列表
# l3 = l1 + l2
# print(l3)
# print(l1)
# print(l2)













# test_list = ['a','b','c',1212,23,23,'a',['a','d',[1,2,3]]]
# print(id(test_list))

# test_list[0]="aaa"
# print(test_list)
# print(id(test_list))

#修改嵌套列表
# test_list[-1][0]="dddddd"
# new_list = test_list[-1] # ['a','b']
# print(new_list)
# l1 = new_list[-1]
# print("第三层：",l1)
# new_list[0]='dddddd'
# print(test_list)



#在列表后面追加元素
# test_list.append("py52")
# print(test_list)


#插入元素
# print(test_list[3])
# test_list.insert(1,'py52')
# print(test_list)
# print(test_list[3])



# print(type(test_list))
# print(test_list)
# print(test_list.index("b"))
# print(test_list[0])
# print(len(test_list))
# print(test_list[-1])
# print(test_list[7])
# test_str = "python"
# print(test_str[::-1])
# print(test_list[::-1])
# print(test_list[0:3])





