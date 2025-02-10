"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/6/22 19:59
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
运算符
一、算数运算符
1、加、减、乘
2、除：得到浮点数(10/2)、取整(10//3)商的整数部分
3、取模(取余数): 10%3
4、幂运算: 2**3

二、赋值运算符
1、=：num = 10
2、num *= 10
3、num += 10

三、比较运算符,返回布尔值
1、>、< 、== 、>=、<= 、!=

四、逻辑运算
1、与(and): 多个条件都成立返回True，否则返回False
   print(num != 10 and num == 110 )
2、或(or)：只要有一个条件为True，就返回True，否则返回False
   print(num != 10 or num == 110 )
3、非(not)：对结果进行取反
   print(not num == 10)

五、成员运算
1、字符串的时候再讲

六、身份运算
1、id(num1)获取内存地址
2、比较内存地址：print(num1 is num2)  
3、is not


七、优先级
1、乘、除、取余、取整
2、加、减
3、比较运算: >、<、>=、
4、比较等号：== !=
5、赋值运算
6、身份运算
7、成员运算
8、逻辑运算
9、提高优先级()



"""
a,b = 10,20

print(a)
print(b)




# ==：比值  is：内存地址(是否是同一个东西)

# num1=10
# num2=10
# res1 = id(num1)
# print(res1)
# res2 = id(num2)
# print(res2)


#用来理解代码执行
# print(num1 is num2)
# print(num1 == num2)



# num = 10
      # True       True
# print(num != 1 and num == 10 )
# print(num != 10 or num == 110 )

#True

# res = not num == 10
# print(res)


str1 = "hello Python"


#赋值运算
# num = 10
#先运算再赋值
# num *= 10  # num = num + 10
# print(num)







#算数运算
# print(10/3)
# print(10//3)
# print(10%3)
# print(2**3)


