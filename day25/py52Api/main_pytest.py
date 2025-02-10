"""
============================
Project: py52Api
Author:柠檬班-海励
Time:2022/9/26 21:27
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、allure测试报告
1、通过allure系统去渲染自己能识别的文件
2、安装插件
   pip install allure-pytest==2.9.43
3、安装jdk1.8
4、创建一个保存allure测试报告文件的目录
5、下载allure服务程序，解压即可，配置环境变量(系统环境变量)
   D:\ProgramFiles\allure-2.13.2
6、运行自动化框架，让他生成测试报告文件
7、启动allure服务(进入项目的rootdir目录下执行命令)
   allure serve reports\allurefile
8、参数
pytest.main(['-sv','test_cases/test_8_pytest.py','--clean-alluredir','--alluredir=reports/allurefile'])
#alluredir=相对路径，相对rootdir
#--clean-alluredir：清除上一次生成的测试报告文件
#设置allure测试报告文件生成的目录
"""

import pytest

#rootdir
#alluredir=相对路径，相对rootdir
#--clean-alluredir：清除上一次生成的测试报告文件
#设置allure测试报告文件生成的目录
pytest.main(['-sv','test_cases/test_8_pytest.py','--clean-alluredir','--alluredir=reports/allurefile'])






