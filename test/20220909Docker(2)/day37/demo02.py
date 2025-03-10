"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/9/9 20:25
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
jenkins镜像命令
docker pull qinhaili/new_enkins:haili

python镜像命令
docker pull qinhaili/python3:haili

一、docker镜像命令
1、查看镜像
docker images
2、查看镜像

3、拉取镜像
在这里找镜像(docker hub)
https://hub.docker.com/_/python/tags
docker pull 镜像名称:标签
如果拉取镜像的时候不加标签，默认拉取最新的镜像，标签为latest

4、搜索镜像
不能直接找到对应的详细版本信息，只能去网站上去找
docker search 镜像名称

5、删除镜像
docker rmi 镜像名称:标签 
docker rmi -f  镜像名称:标签 
docker rmi 镜像id

6、修改镜像名称docker tag 老镜像名称::标签 新镜像名称:标签
docker tag python:3.10.7-alpine python3.10.7:haili





"""