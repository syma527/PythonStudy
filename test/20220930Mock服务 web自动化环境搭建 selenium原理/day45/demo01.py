"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/9/30 20:02
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、unittest自带的mock模块
使用场景：合作开发脚本或者框架，其他同事接口没有实现，自己Mock返回值
from unittest import mock
def demo01():
    pass
demo01 = mock.Mock(return_value={"key":"name"})
res = demo01()
print(res)


二、fastmock平台
1、网站(要注册)
https://www.fastmock.site/#/project/783667f6d6afa2dc7b0deb3308302c3e
2、添加项目
3、添加接口并设置返回值


三、flask(Django)
1、安装专业版的pycharm
2、安装flask框架
   pip install flask
3、创建flask项目
   
4、代码
from flask import Flask,jsonify
app = Flask(__name__)

#接口地址
# @app.route('/login/user')
def hello_world():
    return 'Hello World!'
#接口地址
# @app.route('/login/python')
def hello_python():
    return jsonify({"code":"200"})

app.add_url_rule("/login/user",view_func=hello_world,methods=['get','post'])
app.add_url_rule("/login/python",view_func=hello_python,methods=['get','post'])

if __name__ == '__main__':
    app.run()

name = '' or 1=1
select *from user  where name = f'{name}'
select * from user  where name = '' or 1 = 1




"""
from unittest import mock
def demo01():
    pass

demo01 = mock.Mock(return_value={"key":"name"})

res = demo01()
print(res)





