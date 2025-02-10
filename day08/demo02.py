1"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/4 20:34
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、嵌套循环
1、嵌套循环的分类
for + for 
for + while
while + while
2、外层循环执行一次，内层循环执行一遍


"""

# 99乘法表,拓展知识，不影响做自动化测试
# 纵向是外层循环，横向是内层循环
#外层循环竖排
for i in range(1,10):
    #内层循环横排  range(1,2)  range(1,3)  range(1,4)  == i + 1
    for k in range(1,i+1):
        # print(k*i=k*i) end = "" 不换行输出
        print("{}x{}={}\t".format(k,i,k*i),end="")
    #内存循环每次结束之后要换行输出
    print()









"""
n = 0
while n < 10:
    print("外层循环的值：",n)
    num = 0
    while num < 5:
        print("内层循环的值：",num)
        num += 1
    n += 3



for i in range(3):
    print("外层循环的值：",i)
    num = 0
    while num < 5:
        print("内层循环的值：",num)
        num += 1


for i in range(3):
    print("外层循环的值：",i)
    for j in range(3):
        print("内层循环的值：",j)



"""



