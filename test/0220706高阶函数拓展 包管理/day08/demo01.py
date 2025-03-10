"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/4 20:07
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
for  while
一、range函数
作用：用于生成一个可迭代对象
语法：range(起始索引值,结束索引值,步长)

二、循环控制关键字
1、continue: 结束本次循环,进入下一轮循环
for  i in range(10):
    if i == 5:
        continue
    print(i)
    
2、break：退出循环
for  i in range(10):
    if i == 5:
        break
    print(i)
    
    
三、for循环和while循环的使用场景
1、知道循环次数的时候用for循环
2、不知道循环次数的时候用while循环
import random
num = 0
while num < 10:
    print("num的值",num)
    n = random.randint(1, 10)
    print("随机生成数=：",n)
    num += n
"""









"""
import random
num = 0
while num < 10:
    print("num的值",num)
    n = random.randint(1, 10)
    print("随机生成数=：",n)
    num += n



for  i in range(10):
    if i == 5:
        continue
    print(i)


for  i in range(10):
    if i == 5:
        break
    print(i)



for i in range(1,5,2):
    print(i)
print("="*30)
for i in [0,1,2,3,4]:
    print(i)

            # 0   1   2   3
test_list = ['a','b','c','d']

for i in test_list:
    print(i)
print("="*30)
for index in range(4):
    print(test_list[index])
print(list(range(4)))

print("="*30)

for i in range(-1,-5,-1):
    print(test_list[i])
"""