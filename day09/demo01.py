"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/6 20:14
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、拓展
解除嵌套循环
def test():
    for j in range(3):
        print("py52")

for i in range(3):
    print("外层循环")
    test()
    # for j in range(3):
    #     print("py52")

"""

# def test():
#     for j in range(3):
#         print("py52")
#
# for i in range(3):
#     print("外层循环")
#     test()
#     # for j in range(3):
#     #     print("py52")


import sys

for i in sys.path:
    print(i)
test_01()
