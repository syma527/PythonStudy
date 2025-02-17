num = 10
try:
    print("可能报错的代码放这里")
    print(num1)
except Exception as e:
    print("报错后执行的代码放这里")
    # raise AssertionError("py23")
    raise Exception("手动抛出的异常")