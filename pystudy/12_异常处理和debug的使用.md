# 异常处理

概念：

什么是异常： 程序或者代码在执行过程中报错了，无法继续执行了，这就叫异常

## 一、常见的异常

NameError: name 'name' is not defined

## 二、异常捕获

try：

​	print("可能报错的代码放这里")

​	print(num)

except:

​	print("报错之后执行代码放这里")

​	print(num)





num  = 10

try:

​	print("可能报错的代码放这里")

​	print(num)

except:

​	print("报错后执行的的代码放这里")

​	print(num)

else：

​	print("执行没有报错的时候执行的代码")



```
try:
	print("可能报错的代码放这里")
	print(num)
except:
	print("报错后执行的代码放这里")
	print(num)
else:
	print("执行后报错的时候执行的代码")
finally:
	print("不管是否报错都会执行的代码")
```

## 自定义异常

使用场景：unittest断言原理，他是以程序执行过程中是否抛出异常，如果抛出异常就认为用例执行失败，没抛出异常认为成功

```
num = 10
try:
	print("可能报错的代码放这里")
	print(num1)
except Exception as e:
	print("报错后执行的代码放这里")
	#手动抛出异常
	raise AssertionError("py22")
	raise Exception("手动抛出的异常")
	
```

```
num = 10
try:
	print("可能报错的代码放这里")
	print(num1)
except Exception as e:
	print("报错后执行的代码放这里")
	#手动抛出异常
	#raise AssertionError("py43")
	raise Exception("手动抛出的异常")
```

# debug

1、step over: 下一步

2、step into：进入函数内部

3、resume program： 到下一个断点处

4、step into my code: 从源码处回到自己写的代码里面

5、run to cursor: 断点听到鼠标聚焦的位置  // 鼠标放置的位置就是断点处，**不常用**



```
from day10.demo02 import test_01

def test_03():
	print("test_03")
	test_02()
	print("test_03")
	user_info = test_01()
	print("sddsdsdddddddd")
	print(user_info)

def test_02():
	print("test_02")
	print("test_02")
	print("test_02")
```

