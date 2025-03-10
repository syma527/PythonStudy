"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/9/30 21:22
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""


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



