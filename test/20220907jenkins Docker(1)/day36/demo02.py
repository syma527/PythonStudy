"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/9/7 21:20
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、概念
1、虚拟化：一种资源管理技术
  虚拟机(安装centos虚拟机)、内存管理、硬盘分区管理、
   
2、docker是什么
  虚拟容器技术：docker是虚拟化技术的一种，虚拟容器技术，模拟一个极小的linux系统(dockerfile)
  沙箱机制：基于一个exe文件创建的应用，都是相互独立的
  镜像：好比是在windows创建centos系统的.iso镜像文件，在docker里面，镜像文件
  容器：基于docker镜像创建出来的系统(相当于.iso镜像创建的linux系统)
   windows --- 虚拟技术(vmware软件)--- .iso镜像文件 --- 得到一个centos系统
   linux --- 虚拟技术(docker软件)--- 镜像文件(特别小) --- 得到一个centos系统
   
二、docker安装
https://docs.docker.com/engine/install/
卸载之前的docker清理环境
sudo yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine

查看linux信息(确认是否是centos)
lsb_release -a

1、yum包更新到最新
sudo yum update

一、手动安装
1、安装需要的软件包yum-util 提供yum-config-mamager功能，另外两个是devicemapper驱动依赖的
sudo yum install -y yum-utils

2、设置yum源为阿里云(速度更快)
yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo

3、安装docker(docker-ce社区版免费)
yum -y install docker-ce docker-ce-cli containerd.io

4、安装后查看docker版本
docker -v

5、设置ustc镜像站点(指定注册中心地址)
安装完之后这个文件是空的
vim /etc/docker/daemon.json
{
"registry-mirrors":["https://docker.mirrors.ustc.edu.cn"]
}

6、脚本安装
1、安装发布版本
curl -fsSL https://get.docker.com -o get-docker.sh -o test-docker.sh
sh get-docker.sh


二、docker优点
1、快速的构建环境
2、资源占用很少
3、运维更简单了
4、一台机子可以创建N个容器，合理利用资源节约资源

三、平时的应用
1、部署测试环境，生成环境，验收环境
2、微服务结构
3、自动化项目的部署


四、docker启动与停止
1、启动docker服务
systemctl start docker
2、停止docker服务
systemctl stop docker
3、重启
systemctl restart docker
4、查看docker状态
systemctl status docker
5、查看docker版本
docker -v
6、开机自动启动
systemctl enable docker

"""



