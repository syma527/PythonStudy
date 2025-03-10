"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/9/21 20:34
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
import pytest


#这里的测试用例文件使用的是相对路径，基于rootdir的相对路径
#rootdir的路径是pytest.main()函数执行的目录的路径
# pytest.main(['-s','-v','test_demo.py'])

#如果不指定测试文件(py文件)，会默认去rootdir下面去收集test_开头或者_test结尾的文件里面的测试用例
# pytest.main()


pytest.main(['-s','-v','demo04.py'])






