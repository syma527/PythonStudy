import traceback
num = 10
try:
    print("可能报错的代码放这里")
    print(num1)

except Exception as e:
    print("报错后的代码放这里")
    #手动抛出异常
    raise AssertionError("py31")
   # raise Exception("手动抛出的异常")