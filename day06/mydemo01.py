"""dict1 = {'name': 'tom', 'age': 19, 'gender': '女'}

# print(dict1)

dict1['key'] = 'qwer'
# print(dict1)


dict1.update({'math':78,'chinese':67,'english':89})

# print(dict1)




print(dict1.values())"""
from time import process_time_ns
#
# box = {'red':1,'blue':2}
#
# photo = list(box.values())
# monitor = box.values()
# print(photo)
#
# print(list(monitor))
#
#
# box['green'] = 3
#
# print(photo)
# print(list(monitor))

# box = {'red':1,'blue':2}
#
# for key in box.keys():
#     print(key)
#
# for values in box.values():
#     print(values)
#
# for key in box.items():
#     print(key)



# expect_code = [200,400,300,500]
#
# actually_code = [200,300,403,500]
# error_count = []
# for i,(expect,actuall) in enumerate(zip(expect_code,actually_code),start =1):
#     if expect != actuall:
#         # raise  AssertionError(f"测试用例第{i} 失败,期望{expect},实际{actuall}")
#         error_msg = f'测试用例第{i} 失败,期望{expect},实际{actuall}'
#         error_count.append(error_msg)
#
# full_error_message = "发现以下 {} 个错误:\n".format(len(error_count)) + "\n".join(error_count)
# raise AssertionError(full_error_message)


dict1 = {i:i**2 for i in range(1,5)}
# print(dict1)

set1 = {i**2 for i in range(10)}

print(set1)

