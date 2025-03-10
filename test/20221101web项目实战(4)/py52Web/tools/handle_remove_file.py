"""
============================
Project: py52Web
Author:柠檬班-海励
Time:2022/11/1 21:45
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
import os

from tools.handle_path import error_image_dir


class HandleRemoveFile:
    @classmethod
    def remove_file(cls):
        #获取到目录下的文件名称
        name_list = os.listdir(error_image_dir)
        #删除指定规则的文件(.png结尾的文件)
        for name in name_list:
            if name.endswith(".png"):
                file_name = os.path.join(error_image_dir,name)
                os.remove(file_name)
                print("错误截图删除成功")
            else:
                print("不是png文件,不需要删除")


# HandleRemoveFile.remove_file()