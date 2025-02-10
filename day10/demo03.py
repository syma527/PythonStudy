"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/8 20:33
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
二、异常处理
概念：
什么是异常：程序或者代码在执行过程中报错了，无法继续执行了，这就叫异常


三、常见的异常
NameError: name 'name' is not defined


四、异常捕获
try:
    print("可能报错的代码放这里")
    print(num)
except:
    print("报错之后执行的代码放这里")
    print(num)
    
    
num = 10
try:
    print("可能报错的代码放这里")
    print(num)
except:
    print("报错之后执行的代码放这里")
    print(num)
else:
    print("执行没有报错的时候执行的代码")
    

try:
    print("可能报错的代码放这里")
    print(num)
except:
    print("报错之后执行的代码放这里")
    print(num)
else:
    print("执行没有报错的时候执行的代码")
finally:
    print("不管是否报错都会执行的代码")

五、自定义异常
使用场景：unittest断言原理，他是以程序执行过程中是否抛出异常，
        如果抛出异常就认为用例执行失败，没抛出异常认为成功
num = 10
try:
    print("可能报错的代码放这里")
    print(num1)
except Exception as e :
    print("报错之后执行的代码放这里")
    #手动抛出异常
    raise AssertionError("py51")
    raise Exception("手动抛出的异常")
"""
import traceback

num = 10
try:
    print("可能报错的代码放这里")
    print(num1)
except Exception as e :
    print("报错之后执行的代码放这里")
    #手动抛出异常
    raise AssertionError("py51")
    raise Exception("手动抛出的异常")




