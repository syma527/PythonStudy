"""
============================
Project: AAAAA
Author:柠檬班-海励
Time:2022/10/27 21:23
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
import json
import base64
import requests
from PIL import Image

class GetImageCode:

    def save_web_img(self,driver):
        """web页面截图"""
        driver.save_screenshot('code1.png')

    def save_code_img(self,img_element):
        """将验证码截图出来"""
        # from PIL import Image
        # 乘以屏幕缩放比例125%，每个电脑不一样
        left = img_element.location['x'] * 1.25
        top = img_element.location['y'] * 1.25
        right = (img_element.location['x'] + img_element.size['width']) * 1.25
        bottom = (img_element.location['y'] + img_element.size['height']) * 1.25
        im = Image.open('code1.png')
        im = im.crop((left, top, right, bottom))
        im.save('code.png')

    def get_image_code(self,b64, uname="haili", pwd="QINHAILI", typeid=3):
        """请求第三方系统解析验证码"""
        data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
        result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
        if result['success']:
            return result["data"]["result"]
        else:
            return result["message"]

    def get_code(self,code_img_name):
        """读取验证码图片,调第三方系统解析验证码"""
        with open(file=code_img_name, mode="rb") as f:
            img_byte = f.read()
            base64_data = base64.b64encode(img_byte)
            b64 = base64_data.decode()
            # 获取图片验证码
            code_num = self.get_image_code(b64=b64)
            print("图片验证码:", code_num)
            return code_num

cl =   GetImageCode()
from selenium import webdriver

dr = webdriver.Chrome()
dr.get(url="http://mall.lemonban.com/admin/#/login")
dr.implicitly_wait(20)
#用户名输入框
dr.find_element_by_xpath('//input[@placeholder="用户名"]').send_keys("student")
#密码输入框
dr.find_element_by_xpath('//input[@placeholder="密码"]').send_keys("123456a")
#定位图片
img_element = dr.find_element_by_xpath('//div[@class="mid"]//img')
#验证输入框
code_input = dr.find_element_by_xpath('//input[@placeholder="验证码"]')

#保存web页面截图
cl.save_web_img(driver=dr)

#保存验证码截图
cl.save_code_img(img_element=img_element)

#获取图片验证码
code_num = cl.get_code(code_img_name="code.png")

#输入图片验证码
code_input.send_keys(code_num)

#点击登陆
dr.find_element_by_xpath('//input[@value="登录"]').click()




