"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/9/28 20:48
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""

一、windows下生成allure测试报告
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


二、jenkins容器生成allure测试报告
1、在jenkins中安装allure插件
2、allure-2.13.2复制到jenkins容器中，配置好环境变量(直接配置到jenkins的allure插件里面)
   1、docker cp allure-2.13.2 py52jenkins:/mnt/
   2、vi /etc/profile
   3、英文模式下输入i，进入编辑模式
      export PATH=$PATH:/mnt/allure-2.13.2/bin
   4、切换到命令行模式：shift+冒号(英文模式),输入wq保存文件
   5、重新加载配置文件: source /etc/profile
   6、退出容器
3、在插件里面配置命令
4、jdk不需要单独安装，jenkins已经有了jdk

三、排错总结
1、start.sh 里面
   docker run --rm -w=$WORKSPACE --volumes-from=py52jenkins pythondemo:haili
   中的python容器没有，因为我删掉了
   解决方案: 重新打一个名称为pythondemo:haili的镜像，打镜像的时候修改了cmd里面的命令
   Unable to find image 'pythondemo:haili' locally
   
2、start.sh 里面
   docker run --rm -w=$WORKSPACE --volumes-from=py52jenkins pythondemo:haili
   --volumes-from=py52jenkin容器名称用错了，之前上课用的是另外一个容器，我也删了
   开始创建python镜像执行python自动化测试
    docker: Error response from daemon: No such container: pyjenkins.
    See 'docker run --help'.
    
3、打好的python镜像没有pytest相关的依赖包
   重新打镜像，把依赖包增加进来
   Traceback (most recent call last):
    File "/var/jenkins_home/workspace/py52Api/main_pytest.py", line 31, in <module>
    import pytest
    ModuleNotFoundError: No module named 'pytest'

4、jenkins里面allure测试报告的目录配错了
   修改回来就行: reports/allurefile
   /mnt/allure-2.13.2/bin/allure generate -c -o /var/jenkins_home/workspace/py52Api/allure-report
   allure-results does not exists
   


跨服务器拷贝文件：
scp -r allure-2.13.2 root@192.168.1.180:/mnt/
回车输入密码，就会复制过去




"""


