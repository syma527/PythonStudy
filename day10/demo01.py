"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/8 19:57
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
from demo02 import test_01

"""
一、模块导入
1、python自带的包或者模块
2、第三方包(库)
3、自定义包(模块)

二、导入场景
自动导包：alt+回车

1、同一个包下面导入模块
   1、导入模块
      import demo02
   2、导入指定的对象
      from day10.demo02 import test_01
      from day10.demo02 import test_01,name
2、跨包导入其他包的模块
      from day09.demo04 import demo01
      import day09.demo04 as demo
3、跨项目导入模块
      from 项目名称.day09.demo04 import demo01
      import 项目名称.day09.demo04 as demo
      
三、注意点
1、自定义模块的时候，命名一定不能用关键字
2、导包出错了怎么排查问题
   1、看你自己的解释器用的是哪个版本
   2、你的包在不在python默认的目录下
      1、动态添加
         import sys
         print(sys.path)
         sys.path.append("你的目录")
      2、标记为资源
         Mark Directory as >> source root

"""
"""
# import demo02
# from day10.demo02 import test_01,name


# test_01()
# print(name)

# from day09.demo04 import demo01

import day09.demo04 as demo
demo.demo01()
"""

# import demo02
#
#
#
# demo02.test_01()
#
#
#
# # import sys
# print(sys.path)
# sys.path.append("你的目录")

info = ["yuze", 18, '男', "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]
# print(info)
# del info[3]
# print(info)
print(info)
# res = info.pop(3)
#
# print(res,"\n",info)
info.remove("矮穷丑")
print(info)

