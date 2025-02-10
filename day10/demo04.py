"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/8 21:13
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
三、debug进阶
1、step over: 下一步
2、step into：进入函数内部
3、resume program: 到下一个断点处
4、step into my code：从源码处回到自己写的代码里面
5、run to cursor：断点停到鼠标聚焦的位置
"""


from day10.demo02 import test_01

def test_03():
    print("test_03")
    test_02()
    print("test_03")
    user_info = test_01()  # 这里模拟其他接口返回值
    print("uiuyiyuuyir") #
    print(user_info) #使用其他接口的返回值

def test_02():
    print("test_02")
    print("test_02")
    print("test_02")


test_03()



