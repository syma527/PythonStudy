"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/9/14 20:01
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
语法规则
指令大小写不敏感，为了区分习惯上用大写
Dockerfile非注释行第一行必须是FROM
文件名必须是Dockerfile
Dockerfile指定一个专门的目录为工作空间
所有引入映射的文件必须在这个工作空间目录下
Dockerfile工作空间目录下支持隐藏文件(.dockeringore)
(.dockeringore)作用是用于存放不需要打包导入镜像的文件，根目录就是工作空间目录
每一条指令都会生成一个镜像层，镜像层多了执行效率就慢，能写成一条指定的就写成一条

链接：http://testingpai.com/article/1634806562678



windows上执行python接口自动化项目的思路
1、安装python环境
   1、安装python exe 程序，pip 安装依赖包
2、写项目代码
3、cmd 命令行运行python start.py  == pycharm里面右键运行

docker执行python接口自动化项目的思路
1、安装python环境
   实现方案：python容器
   1、自己手动打一个镜像(有项目执行依赖包的镜像)
      1、Dockerfile
   2、通过jenkins从远程仓库将代码拉取到本地，然后放到python容器中执行【写项目代码】
   3、根据自己创建的镜像，创建一个python容器执行我们的项目【指定容器运行的时候执行的命令】

2、jenkins拉取的代码要映射到python容器里面去
   

Dockerfile
基于某个基础镜像来打自己的镜像(根据自己的项目情况安装了某些软件的)
1、Dockerfile的写法(语法)
FROM python:3-alpine  # 第一行非注释行必须是FROM  
WORKDIR /app         #设置容器的工作空间目录
ADD ./xxx.txt /app   #讲宿主机的依赖包文件添加到镜像里面
RUN pip install -r xxx.txt  #安装依赖包，RUN是在打镜像的过程中执行的命令，建议少用RUN
CMD ["python","start.py"]   #创建容器后自动执行的命令，但是如果启动容器的时候传了命令进去，这个命令会被覆盖

2、构建镜像
docker build -t 镜像名称:标签 Dockerfile所在的目录
.:表是当前目录

3、生成依赖包文件
pip freeze > xxx.txt

4、安装依赖包文件中的包
pip install -r xxx.txt



通过jenkins从远程仓库将代码拉取到本地，然后放到python容器中执行【写项目代码】
1、创建一个jenkins容器
docker run -id --name=py52jenkins -p 8809:8080 -u=root -v /usr/bin/docker:/usr/bin/docker -v /var/run/docker.sock:/var/run/docker.sock qinhaili/new_enkins:haili  

将宿主机的docker(docker客户端) 和docker.sock(docker客户端与服务器通讯的文件)映射到jenkins容器，执行docker命令的时候想就相当于在宿主机执行docker命令

2、jenkins构建后执行的命令(jenkins 里面执行的是宿主机的docker命令)
docker run --rm -w=$WORKSPACE --volumes-from=py52jenkins py5220220914:latest
"""




