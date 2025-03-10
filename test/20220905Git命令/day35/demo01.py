"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/9/5 20:22
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""

"""
Git

一、注册Git账号
https://gitee.com/

二、安装客户端
网盘找到git目录下面有
链接：https://pan.baidu.com/s/199Ng3ooyikQ4g14lQO_U9w?pwd=8888 
提取码：8888

三、使用
1、在远程仓库创建一个仓库
2、将远程仓库克隆到本地
  git clone 你的仓库地址
3、将代码复制到本地仓库下面去
4、将代码提交到本地仓库
  git add .   #.表示所有代码
  git commit -am "说明备注信息"
5、将本地仓库的代码提交到远程仓库
  git push
  
三、第一次使用会遇到的问题
git config --global user.email '你注册填的邮箱'
git config --global user.name '你注册的账号'
git push -u origin master 

四、分支相关的命令
1、查看本地分支
git branch
2、查看远程分支
git branch -r 
3、查看远程分支和本地分支的关联关系
git branch -vv
4、查看当前分支的状态
git status
5、创建分支(你在哪个分支上执行的命令，就是基于哪个分支创建的新分支)
git branch 分支名称
6、切换分支(分支一定要是干净的，不能有未提交的代码)
git checkout 分支名称
7、创建并切换到新的分支
git checkout -b 分支名称
8、将本地新分支推送到远程仓库(远程没有该分支的时候用这个命令，如果远程有该分支直接用git push就可以了)
git push --set-upstream origin test02
9、拉取代码(拉取所在分支的代码)
git pull
10、删除分支(本地)
git branch -d 分支名称
11、删除分支(远程)
git push origin --delete 分支名称

五、分支合并
需求：将test01分支合并到master
1、test01提交代码
2、切换到master上
3、git merge test01
4、git push


六、冲突解决
1、什么是冲突
   两个人同时修改了同一行代码(多行)
2、怎么解决重复
   <<<<<<
   ....代码
   ======
   ....代码
   >>>>>>

   1、<<<<<< 到 ====== 是一个分支的代码
   2、====== 到 >>>>>> 是另外一个分支的代码
   3、根据自己的情况，留下一份或者都留下代码
   4、需要删掉：<<<<<< 、======、>>>>>>留你要的代码就行

七、分支回滚
1、查看commit id(提交记录日志)
git log  
2、回滚(根据上一步的commit id)
git reset --hard <commit id>

"""

