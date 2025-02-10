"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/18 21:17
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""

"""
一、上下文管理协议


__enter__()
__exit__()  

"""

class Demo:
    def __enter__(self):
        #前置处理器
        print("调用类的时候会自动执行的方法")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        #后置处理器
        print("执行完成退出的时候会自动执行的方法")

    def test01(self):
        print("干活的人")

if __name__ == '__main__':
    with Demo() as t:
        print(t)
        t.test01()



# import pymysql
#
# with pymysql.connections() as db:
#     pass












