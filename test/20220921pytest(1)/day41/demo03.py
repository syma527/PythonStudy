"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/9/21 21:10
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
数据驱动
case_list = [{},{},{}]

"""

import pytest


case_list = [
             {"id":"1","url":"https://docs.pytest.org/en/stable/1"},
             {"id":"2","url":"https://docs.pytest.org/en/stable/2"},
             {"id":"3","url":"https://docs.pytest.org/en/stable/3"}
             ]

@pytest.mark.parametrize("case",case_list)
def test_01(case):
    print('\n case的数据：',case)


# @pytest.mark.parametrize("id","url",case_list)
# def test_01(id,url):
#     id = id
#     url = url
#     print('\ncase的数据：',id,url)

if __name__ == '__main__':

    pytest.main(['-s','-v'])


