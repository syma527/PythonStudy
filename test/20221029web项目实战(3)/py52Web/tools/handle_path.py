"""
============================
Project: py52Web
Author:柠檬班-海励
Time:2022/10/24 21:53
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
import os
import time

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)

#错误截图路径
error_image_dir = os.path.join(base_dir,"error_images")
print(error_image_dir)


#日志路径
log_file_name = time.strftime("%Y%m%d",time.localtime())
log_dir = os.path.join(base_dir,"logs",f"{log_file_name}.log")


#上传图片路径
image_dir = os.path.join(base_dir,"images","py52.png")





