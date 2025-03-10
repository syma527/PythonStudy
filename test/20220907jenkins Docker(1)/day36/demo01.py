"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/9/7 20:01
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
免安装版本、服务器版本、linux下安装版本(软件)、docker版本(服务)
http://testingpai.com/article/1644570535388
一、jenkins(本地的jenkins)【了解】
1、下载海励老师百度网盘的jenkins+jdk
2、安装jdk，配置好环境变量(系统环境变量，不要配用户环境变量)
3、通过命令启动Jenkins.war
   端口使用8000以上的端口，因为8000一下默认是系统使用的端口，可能会冲突
   java -jar Jenkins.war --httpPort=9999
4、打开浏览器访问: http://localhost:9999/
   初始化需要等待2分钟左右，然后获取到初始化密码，点继续
5、不要安装插件，点右边的【选择插件来安装】
6、新手入门页面，点无，再点安装
7、设置登陆账号和密码

二、jenkins工作原理【掌握】
1、job(items)：任务，你要做的事情以任务的形式出现的jenkins里面
2、工作空间：存放你任务的数据的地方
3、插件：jenkins是通过插件来拓展功能的

三、创建job【掌握】
1、创建job(自由风格的任务)
2、配置git仓库地址、账号、密码
3、配置构建后的操作命令(把代码拉下来之后运行代码)

四、插件安装【掌握】
入口：ManageJenkins ---》ManagePlugins
1、Git plugin
2、HTML Publisher plugin


五、centos7虚拟机安装
http://testingpai.com/article/1629981536584





"""