"""
num = 999

try:
    print("可能报错的放在这里")
    print(num1)
except:
   print("如果报错放在这里")
   print(num)


num = 10
try:
    print("可能报错的代码放这里")
    print(nu)
except Exception as e:
    print("报错后执行的代码放这里")
    raise AssertionError("py52")


num = 10
num2 = 33
try:
    print("可能报错的代码放这里")
    print(num2)
except:
    print("报错后执行的代码放这里")
    print(num)
else:
    print("执行没有报错的时候执行的代码")

"""

num = 10
try:
    print("可能报错的代码放在这里")
    print(num1)
except:
    print("如果报错了放在这里")
    print(num)
finally:
    print("不管是不是报错最后都会执行")