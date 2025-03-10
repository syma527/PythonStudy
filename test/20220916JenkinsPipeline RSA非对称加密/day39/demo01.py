"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/9/16 20:27
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
了解即可：
jenkinsPipeline语法说明：
https://www.jenkins.io/zh/doc/book/pipeline/syntax/#post


测试报告插件
http://testingpai.com/article/1630998822695
Startup Trigger
Groovy
安装插件Startup Trigger: 可实现在Jenkins节点(master/slave)启动时触发构建
安装插件Groovy: 可实现直接执行Groovy代码
来到任务配置页面在“构建触发器(Build Triggers)”模块，选择“Buildwhen job nodes start”选项
在“构建（Build）”模块，选择“Execute system Groovy script”，执行如下Groovy命令：System.setProperty("hudson.model.DirectoryBrowserSupport.CSP","")


jenkinspipeline项目使用
http://testingpai.com/article/1644826809349
1、安装插件
pipeline
2、创建pipeline项目
3、配置项目
   1、找到pipeline，配置git仓库
   2、只要你不修改Jenkinsfile文件的名称，其他的不用配置
4、手动配置HTML测试报告展示的脚本
"""