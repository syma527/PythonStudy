"""
============================
Project: py52Api
Author:柠檬班-海励
Time:2022/8/19 20:54
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
import os

#项目根路径
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_path)

#测试数据路径
case_data_dir = os.path.join(base_path,"test_datas","case_data.xlsx")

#测试用例路径
case_dir = os.path.join(base_path,"test_cases")

#日志路径
log_dir = os.path.join(base_path,"logs")

#测试报告路径
report_dir = os.path.join(base_path,"reports")

#图片路径
image_dir = os.path.join(base_path,"images","py52.png")

print(image_dir)