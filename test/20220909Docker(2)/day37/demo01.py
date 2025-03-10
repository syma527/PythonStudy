"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/9/9 20:01
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、Centos机子无法上网
1、原因：没有配置网卡文件，共享宿主机的网卡设备
2、解决方案
   1、vmware的网络适配器，设置为NAT 或者 桥接模式都可以
   2、创建网卡文件
     目录：cd /etc/sysconfig/network-scripts/
     查看是否有：ifcfg-ens33 或者 ifcfg-ens32，如果没有就创建该文件(没有后缀)
3、修改ifcfg-ens33/ifcfg-ens32 文件内容
#桥接模式
TYPE="Ethernet"
PROXY_METHOD="none"
BROWSER_ONLY="no"
BOOTPROTO="dhcp" #如果是桥接模式dhcp自动获取，如果是NAT：static
DEFROUTE="yes"
IPV4_FAILURE_FATAL="no"
IPV6INIT="yes"
IPV6_AUTOCONF="yes"
IPV6_DEFROUTE="yes"
IPV6_FAILURE_FATAL="no"
IPV6_ADDR_GEN_MODE="stable-privacy"
NAME="ens33"
UUID="784d0f02-9840-411b-afc1-9d65850bd9dd"
DEVICE="ens33"
ONBOOT="yes"

#NAT模式需要加这些 + 桥接模式
DNS1=8.8.8.8
DNS2=223.5.5.5
GATEWAY=192.168.1.2  #最后配2，用来转发
NETMASK=255.255.255.0
IPADDR=192.168.1.180

4、重启网卡
systemctl restart network.service

5、输入命令看IP地址
ifconfig

二、网卡是正常的但是访问不到虚拟机
1、在没有停机的情况下，切换了网络
2、解决方案重启网卡
systemctl restart network.service

"""