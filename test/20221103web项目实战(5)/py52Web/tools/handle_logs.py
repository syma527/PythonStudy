"""
============================
Project: py52Web
Author:柠檬班-海励
Time:2022/11/3 20:12
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
import logging

from tools.handle_path import log_dir


from logging import handlers


def my_log():
    #1、创建日志收集器
    py52 = logging.getLogger(name="py52")

    #2、创建日志输出渠道
    pycharm = logging.StreamHandler()  # 1.log,2.log
    #文件渠道
    log_file = handlers.TimedRotatingFileHandler(filename=log_dir,interval=1,when="D",backupCount=20,encoding="utf-8")

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

my_log = my_log()