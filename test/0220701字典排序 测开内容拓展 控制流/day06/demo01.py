"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/6/29 20:08
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
集合【不用】

一、特性
1、无序
2、不能通过索引访问
3、元素不可以重复
4、可迭代的
5、不可嵌套

二、创建
test_set = {1,1,22,22,'a',55,55,'a','c','c','v'}

三、修改
1、添加元素
test_set.add('a')
2、添加一个可迭代对象进来
test_set.update(test_list)

四、删除
1、删除指定元素
test_set.remove('a')
2、pop删除随机删
test_set.pop()
3、清空
test_set.clear()

五、去重【掌握】
1、原理：先转化成set类型，set类型的特点就是元素不可重复
2、去重之后会改变列表，元组的顺序
3、应用场景：
   1、列表去重
   2、元组去重

"""
test_set2={}
print(test_set2,type(test_set2))



# test_set = {1,2,3,4,'a','a',1,2,3,4}

#不可嵌套
# test_set2 = {{1,2,3},{4,5,6}}
# print(test_set2)


# [1, 2, 3, 4, 'a']
# test_set = (1,2,3,4,'a','a',1,2,3,4)
# print(tuple(set(test_set)))

# test_str = "pythhhhhon"

# reslut = list(set(test_set))
# print(reslut)
# print(test_set)

"""
test_set = {1,2,3,4,'a','a',1,2,3,4}
test_set.remove('a')
test_set.pop()
test_set.clear()

print(test_set)




# test_set.add('a')

test_set.update(test_list)
print(test_set)




# test_set = {1,22,2,'a',55,78,'bb','c',23,'v'}
test_set = {1,1,22,22,'a',55,55,'a','c','c','v'}
print(type(test_set))
print(test_set)
for i in test_set:
    print(i)

"""
