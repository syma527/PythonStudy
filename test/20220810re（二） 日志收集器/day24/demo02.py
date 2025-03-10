"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/8/10 19:59
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
二、日志收集器
1、日志的作用：记录程序执行过程，还原用户操作

2、日志的要素
日志级别：日志的类型(正常运行输出的日志、调试输出的日志、警告提示日志、错误日志、系统崩溃)
         debug < info < warning < error < critical 
日志渠道：日志输出的地方
日志格式：日志输出呈现出来的格式
日志内容：日志要表达什么，记录什么

2022-08-10-INFO-test.java-no 30: 用户登陆

三、自定义日志收集器
1、日志格式
%(name)s       日志渠道的名称
%(levelno)s    日志级别对应的数字编号
%(levelname)s  日志级别的名称
%(pathname)s   输入日志的py文件的绝对路径
%(filename)s   输出日志的py文件名称(带.py)
%(module)s     输出日志的模块文件名称(不带.py)
%(lineno)d     输出日志的行，或者是报错是哪一行(行号)
%(funcName)s   输入日志的函数是哪一个
%(created)f    日志输出的时间
%(asctime)s    日志输出时间(精确到毫秒 年-月-日 时:分:秒,毫秒)
%(msecs)d      日志输出时间的毫秒部分
%(relativeCreated)d 日志输出的相对时间(模块加载+执行到你这个日志输出这行)
%(thread)d      线程的id号
%(threadName)s  线程名称
%(process)d     进程的id号
%(message)s     日志内容

2、文件收集器
1、filename：日志文件(加路径，如果不加路径默认是当前文件所在目录)
2、encoding：处理中文乱码
3、backupCount：保留日志文件的个数
4、interval：滚动周期,根据when的取值，生成不同的日志文件周期
5、when: h
"""

import logging
import time

from logging import handlers

def my_log():
    #1、创建日志收集器
    py52 = logging.getLogger(name="py52")

    #2、创建日志输出渠道
    pycharm = logging.StreamHandler()  # 1.log,2.log
    #文件渠道
    log_file = handlers.TimedRotatingFileHandler(filename=f"{int(time.time())}.log",interval=1,when="D",backupCount=20,encoding="utf-8")

    #3、日志格式
    ft = ">>>%(asctime)s-%(name)s-%(levelname)s-%(filename)s: %(message)s "
    log_style = logging.Formatter(fmt=ft)

    #4、日志格式绑定(渠道)
    pycharm.setFormatter(fmt=log_style)
    log_file.setFormatter(fmt=log_style)

    #5、设置日志级别(收集器的日志级别(大)debug，输出渠道的日志级别(小)info)
    #一般情况下只设置收集器的日志级别，渠道会继承收集器的日志级别
    # pycharm.setLevel(logging.INFO) #无需设置
    py52.setLevel(logging.DEBUG)

    #6、将日志输出渠道绑定到日志收集器上
    py52.addHandler(pycharm)
    py52.addHandler(log_file)
    return py52

py52 = my_log()


