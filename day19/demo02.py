"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/29 20:59
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""

"""
数据共享
对自动化来说没有作用，了解即可

"""

from faker import Faker

class Demo:
    def __init__(self):
        self.fk = Faker(locale="zh-cn")

    def test_01(self):
        Faker.seed(123)
        phone = self.fk.phone_number()
        print(phone)

    def test_02(self):
        Faker.seed(123)
        phone = self.fk.phone_number()
        print(phone)

if __name__ == '__main__':
    cl = Demo()
    cl.test_01()
    cl.test_02()
