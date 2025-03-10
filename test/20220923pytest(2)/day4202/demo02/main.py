"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/9/23 21:43
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""


"""
1、conftest.py所在的目录子目录可以使用，和conftest.py是兄弟目录下的可以使用
2、conftest.py父目录不能使用
3、一个项目可以有多个conftest，但是不能放同一个目录下

"""
import pytest

@pytest.mark.usefixtures("init_func2")
def test_01():
    print("demo02的test_01")

if __name__ == '__main__':
    pytest.main(['-sv'])



