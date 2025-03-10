"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/13 21:21
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
函数执行入口：if __name__ == '__main__':
1、执行当前文件，if __name__ == '__main__':条件成立，会执行if下面的代码块
2、将当前文件导入到其他模块执行，if __name__ == '__main__':条件不成立，不会执行if 下面的代码块


"""
class Demo:
    def test_01(self):
        print("test_01")

print(__name__)
if __name__ == '__main__':
    print(__name__)
    cl = Demo()
    cl.test_01()