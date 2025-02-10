"""
dict1 = {"name": "Alice", "age": 30}
dict2 = {"pwd":"sad123","user":"root"}

test_dict = {"host":"192.168.1.1","port":"2332","user":'root','pwd':"test23"}

res = test_dict.get('host1','test')
print(res)

for i in test_dict.keys():
    print(i)


num = 10
try:
    print("可能报错的代码放这里")
    print(num1)
except Exception as e:
    print("报错后执行的代码放这里")
    #手动抛出异常
except:
    print("手动抛出异常")



num = 10

try:
    print("可能出错的代码放这里")
    print(num)
except:
    print("未出错的代码放这里")
raise Exception("手动抛出异常")

s1 = 'hello'

try:


except IndexError as e:
    print(e)

except KeyError as e:
    print(e)

except ValueError as e:
    print(e)
else:
    print("try内代码块没有异常则执行我")

finally:
    print("无论是否异常，都会执行该模块，通常是进行清理工作")


def add():
    num = 1 + 2
    print(num)
    return num

"""

