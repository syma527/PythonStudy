# for和while的使用

## 一、range函数

作用： 用于生成一个可迭代对象

语法：range（起始索引值，结束索引值，步长）



## 二、循环控制关键字

1、continue: 结束本次循环，进入下一轮循环：

```
for i in range(10):
	if i == 5:
		continue
	print(i)
```

2、break:退出循环

```
for i in range(10):
	if i == 5:
		break
	print(i)
```

## 三、for循环和while循环的使用场景

1、知道循环次数的时候用for循环

2、不知道循环次数的时候用while循环

import random

num = 0

while num < 10:

​	print("num的值", num)

​	n = random.randint(1,10)

​	print("随机生成数=：", n)

​	num += n

```
for i in test_list:
	print(i)
print("*"*30)
for index in range(4):
	print(test_list[index])
print(list(range(4)))


```

## 四、嵌套循环

1、嵌套循环的分类

for + for

for + while

while + while 

2、外层循环执行一次，内层循环执行一遍



```
for i in range(1,10):
	# 内层循环横排，range（1,2） range(1,3)
	for k in range(1,i+1)
	print("{} * {} = {}\t".format(k,i,k*i),end="")
	#end=""不换行输出
	print()
```

while + while

```
n = 0
while n < 10:
	print("外层循环的值",n)
	num = 0
	while num < 5:
		print("内层循环的值",num)
		num += 1
	n += 3
```

for + while

```
for i in range(3):
	print("外层循环的值",1)
	num = 0
	while num < 5:
		print("内层循环的值",num)
		num += 1
	
```

```
for i in range(3):
	print("外层循环的值",1)
	for j in range(3):
		print("内层循环的值",j)
		
```

