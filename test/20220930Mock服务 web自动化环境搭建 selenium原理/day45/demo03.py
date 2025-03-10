"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/9/30 20:43
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、环境搭建
1、安装包
pip install selenium==3.141.0
2、下载驱动
下载地址: http://chromedriver.storage.googleapis.com/index.html


二、selenium原理
1、selenium 客户端==python脚本
2、selenium 服务器==浏览器的驱动程序
3、操作对象 == 浏览器


三、selenium操作浏览器
1、通过webdriver驱动浏览器
2、发送命令打开网站
import time
from selenium import webdriver
import logging
#修改root收集器默认的日志级别
logging.basicConfig(level=logging.DEBUG)
dr = webdriver.Chrome(r'D:\chromeDriver\105\chromedriver.exe')
dr.get(url="http://mall.lemonban.com/admin/#/login")

四、http请求模拟webdriver操作
import requests
from jsonpath import jsonpath
url = "http://127.0.0.1:55340/session"
data = {
	"capabilities": {
		"firstMatch": [{}],
		"alwaysMatch": {
			"browserName": "chrome",
			"platformName": "any",
			"goog:chromeOptions": {
				"extensions": [],
				"args": []
			}
		}
	},
	"desiredCapabilities": {
		"browserName": "chrome",
		"version": "",
		"platform": "ANY",
		"goog:chromeOptions": {
			"extensions": [],
			"args": []
		}
	}
}
#启动浏览器会话
res = requests.post(url=url,json=data)
session_id = jsonpath(res.json(),'$..sessionId')[0]
print(res.json())
#发送请求访问网站
url_login = f"http://127.0.0.1:55340/session/{session_id}/url"
res2 = requests.post(url=url_login,json={"url": "http://mall.lemonban.com/admin/#/login"})


五、操作浏览器
1、退出浏览器
dr.quit()
2、关闭页签
dr.close()
3、最大化
dr.maximize_window()
4、最小化
dr.minimize_window()
5、刷新
dr.refresh()
6、截图
dr.get_screenshot_as_file(r"D:\20220930.png")
7、获取屏幕大小
size = dr.get_window_size()
8、获取cookies信息
cookie = dr.get_cookies()

六、html的组成





"""
import time
from selenium import webdriver
import logging

#修改root收集器默认的日志级别
logging.basicConfig(level=logging.DEBUG)

dr = webdriver.Chrome(r'D:\chromeDriver\105\chromedriver.exe')
dr.get(url="http://mall.lemonban.com/admin/#/login")

dr.maximize_window()

time.sleep(2)

dr.refresh()

time.sleep(2)

size = dr.get_window_size()
print('尺寸：',size)

cookie = dr.get_cookies()
print('cookie:',cookie)

dr.minimize_window()


dr.get_screenshot_as_file(r"D:\20220930.png")

time.sleep(2)

dr.close()



