"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/6 21:35
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""

"""
四、基本概念
模块：在python里面的py文件就叫模块
目录: 目录就是普通的目录(文件夹)
包：有__init__.py文件的目录就叫包

包用来管理模块的

五、模块导入
1、python自带的包或者模块
2、第三方包(库)
3、自定义包(模块)


六、包管理
1、pip用来管理第三方方的包，解决安装包相互依赖的问题
2、常用命令
pip list  查看已安装的第三方包

pip install 包名称 -i http://mirrors.aliyun.com/pypi/simple/  包安装

pip install -U 包名称==v.24.1 更新已有的包,不指定版本号，默认更新到最新版本

pip uninstall 包名称  卸载包

pip list | findstr 包名称    过滤已安装的包，模糊匹配，区分大小写，mac和linux用grep

pip freeze > req.txt  将当前环境用到的包到出到req.txt文件

pip install -r req.txt 根据依赖包文件安装包，如果req.txt文件没有写的包，
                           在安装其他包的时候依赖到某个包，会一起将所有的依赖包安装好
                    
                                        
                       

"""




import demo01
