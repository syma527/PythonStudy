"""
============================
Project: py52Web
Author:柠檬班-海励
Time:2022/11/3 21:28
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
from tools.handle_attribute import HandleAttr
from tools.handle_logs import my_log
import time

from jsonpath import jsonpath
from tools.handle_path import error_image_dir
import os

def outer(func):
    def inner(*args,**kwargs):
        element = None
        retry_count = 0
        page_action = jsonpath(kwargs, '$..page_action')[0]
        try:
            print("装饰器接受到的参数：",args,kwargs)
            element = func(*args,**kwargs)
            my_log.info(msg="装饰器里面被装饰的函数执行成功")
        except Exception as e:
            retry_count += 1
            if retry_count == 3:
                my_log.info(msg="被装饰的函数执行报错,错误次数达到3次，开始截图")
                driver = getattr(HandleAttr, "driver")
                png_name = time.strftime("%Y%m%d_%H%M%S", time.localtime())
                file_name = os.path.join(error_image_dir,f"{page_action}{png_name}.png")
                driver.save_screenshot(filename=file_name)
                my_log.info(msg="截图保存成功")
                raise Exception(e)
            else:
                retry_count = 0
                my_log.info(msg=f"被装饰的函数执行失败,开始重试第:{retry_count}次")
        else:
            my_log.info(msg=f"被装饰的函数执行无报错,元素名称{page_action}")
        finally:
            retry_count = 0
            return element
    return inner





