"""
============================
Project: py52Api
Author:柠檬班-海励
Time:2022/9/5 20:03
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""


"""
移动测试报告文件到历史目录下

"""
import shutil
import os
from tools.handle_path import report_dir,history_dir

class HandleMoveFile:
    @classmethod
    def move_file(cls):
        name_list = os.listdir(report_dir)
        print("reports目录下的文件名称和目录名称",name_list)
        for name in name_list:
            if name.endswith(".html"):
                src = os.path.join(report_dir,name)
                #挪走
                shutil.move(src,history_dir)
                print("html文件挪动成功")

            else:
                print("不是测试报告文件，不挪走")


if __name__ == '__main__':
    HandleMoveFile.move_file()

