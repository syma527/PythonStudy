"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/9/26 20:21
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""

import pytest


#单独收集标记的测试用例，不要在测试用例文件去自动收集执行
# pytest.main(['-sv','demo02.py','-m=py56'])


#逻辑运算 or、and、not
#执行多个标签的用例,or是或者的意思，只要用一个标签都会执行
# pytest.main(['-sv','demo03.py','-m=py56 or login'])

#执行多个标签的用例,and 是和的意思，两个标签都要有才会执行
# pytest.main(['-sv','demo03.py','-m=py56 and login'])

#不执行某个标签的测试用例,只要打了某个不执行的标签，就不会被执行
# pytest.main(['-sv','demo03.py','-m=not py56'])


#执行指定文件的测试用例，或者是测试用例类
# pytest.main(['-sv','demo03.py::test_11'])


#失败重运行
#--reruns：设置重运行的次数
#--reruns-delay：重运行的间隔时间，秒为单位
pytest.main(['-sv','demo01.py','--reruns','2','--reruns-delay','1'])




