"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/9/9 21:08
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
容器命令
1、创建容器
a、交互式方式创建容器
创建容器后自动执行cmd里面的命令
通过docker image inspect python3.10.7:haili可以产看cmd命令是什么
如果退出容器，容器会停止运行
-i：表示以交互式的方式运行容器
-t：分配一个命令行终端
docker run -it --name=py52 python3.10.7:haili
docker run -it --name py52 python3.10.7:haili

b、守护式方式创建容器
/bin/sh：运行容器的时候执行的命令，会覆盖cmd里面的命令
docker run -di --name py52 python3.10.7:haili /bin/sh

2、查看容器
docker ps     #查看正在运行的容器
docker ps -a  #查看所有的容器

3、删除容器
docker rm 容器名称/容器id

4、进入容器里面
docker exec -it py52  /bin/sh
#指定root用户登陆容器，场景是需要执行root用户才能执行的命令的时候
docker exec -it -u 0 py52  /bin/sh
docker exec -it --user root py52  /bin/sh

5、退出容器
exit;

6、容器的启动与停止
启动容器
docker start 容器名称(容器id)
重启容器
docker restart 容器名称(容器id)
停止容器
docker stop 容器名称(容器id)
docker kill 容器名称(容器id)

7、文件拷贝
宿主机文件和容器文件是隔离的
docker cp 宿主机需要拷贝的容器或者目录  容器名称:容器目录
docker cp test.py  py52:/mnt/

8、目录映射
宿主机文件和容器文件相互同步的
docker run -id  -v /mnt/test.py:/mnt/test.py  --name=python52 python3.10.7:haili /bin/sh
docker run -id  -v /mnt/:/mnt/  --name=python52 python3.10.7:haili /bin/sh

"""