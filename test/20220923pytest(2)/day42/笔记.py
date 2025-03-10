"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/9/23 20:08
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""

前后置(夹具)

unittest:
1、函数级别：setup、teardown
2、类级别(类方法)：setupClass、teardownClass

pytest【了解】:
模块级别(py文件)：
setup_module: 模块中第一个测试用例执行之前执行一次
teardown_module: 模块中最后一个测试用例执行之后执行一次

函数级别:
setup_function: 每个测试用例执行之前执行一次
teardown_function: 每个测试用例执行之后执行一次
只对类外面的测试函数生成，类里面的测试用是不生效的

类级别:
setup_class: 每个测试类执行之前执行一次
teardown_class: 每个测试类执行之后执行一次
只对类里面的测试用例生效，类外面的不生效


fixture前置【掌握】
1、语法
fixture命名不要用test开头，要跟测试用例进行区分
命名尽量见文知意

2、参数
scope: 设置前置级别的参数
       function【常用】：默认是函数级别，每个函数执行过程中执行一次
       class【常用】: 类级别，整个类执行过程中只执行一次
       module: 模块级别，在整个模块执行过程中只执行一次
       session：会话级别，在整个会话过程中只执行一次

params：用来做前置后置的参数化的
       接收多个参数(list),list中有多少个元素，前置就会执行多少遍
ids：给每一个params参数的值定义一个别名
autouse=True: 前后置自动调用
name：对前后置进行起别名


多个前置的使用(执行顺序就近原则，靠近测试用例的先执行)
import pytest

@pytest.fixture(scope="class")
def init_login1():
    print("\ninit_login1前置条件")
    yield "success"
    print("\ninit_login1后置处理")

@pytest.fixture(scope="class")
def init_login2():
    print("\ninit_login2前置条件")
    yield "success"
    print("\ninit_login2后置处理")

@pytest.mark.usefixtures("init_login1") #后执行
@pytest.mark.usefixtures("init_login2") #先执行
def test_01(init_login1):
    print("测试用例1")
    test_str = init_login1
    print("参数的使用",test_str)


函数里面使用【了解】
import pytest
@pytest.fixture(scope="function")
def init_login1():
    print("\ninit_login1前置条件")
    yield "success"
    print("\ninit_login1后置处理")
@pytest.mark.usefixtures("init_login2")
def test_01(init_login1):
    print("测试用例1")
    test_str = init_login1
    print("参数的使用",test_str)


类里面使用前后置【掌握】
import pytest
@pytest.fixture(scope="function")
def init_login1():
    print("\ninit_login1前置条件")
    yield "success"
    print("\ninit_login1后置处理")
class TestDemo:
    @pytest.mark.usefixtures("init_login2")
    def test_03(self,init_login2):
        demo = init_login2
        print(demo)
        
       
       
测试用例参数化
1、函数测试用例的参数化【了解】
import pytest
case_list = [
             {"id":"1","url":"https://www.ketangpai.com1"},
             {"id":"2","url":"https://www.ketangpai.com2"},
             {"id":"3","url":"https://www.ketangpai.com3"},
             {"id":"4","url":"https://www.ketangpai.com4"},
           ]
@pytest.mark.parametrize("case",case_list)
def test_04(case):
    print("test_04")
    print(case)
if __name__ == '__main__':
    pytest.main(['-sv'])
    
2、类里面测试用例的参数化【掌握】
import pytest
case_list = [
             {"id":"1","url":"https://www.ketangpai.com1"},
             {"id":"2","url":"https://www.ketangpai.com2"},
             {"id":"3","url":"https://www.ketangpai.com3"},
             {"id":"4","url":"https://www.ketangpai.com4"},
           ]
class TestDemo:
    @pytest.mark.parametrize("case", case_list)
    def test_05(self,case):
        print("测试数据:",case)
if __name__ == '__main__':
    pytest.main(['-sv'])   
    
    
    
yield关键字使用：
http://testingpai.com/article/1636602515232


夹具与参数化在类中的使用
import pytest
#夹具==前后置  yield 与 return
# @pytest.fixture(scope="function")
@pytest.fixture(scope="class")
def init_class():
    num1 = 100
    num2 = 200
    yield num1,num2
    print("后置处理")
case_list = [
             {"id":"1","url":"https://www.ketangpai.com1"},
             {"id":"2","url":"https://www.ketangpai.com2"},
             {"id":"3","url":"https://www.ketangpai.com3"},
             {"id":"4","url":"https://www.ketangpai.com4"},
           ]
@pytest.mark.usefixtures('init_class')
class TestDemo:
    @pytest.mark.parametrize("case", case_list)
    def test_05(self,case,init_class):
        print("测试数据:",case)
        num1,num2 = init_class
        print('前置返回的数据:',num1,num2)

if __name__ == '__main__':
    pytest.main(['-sv'])
    
注意点：
1、@pytest.mark.usefixtures('init_class')可以不写，效果是一样的，但是如果没有写init_class夹具，执行找打不到就会报错
2、建议写上，为了增强代码的可读性
3、一套框架要使用同一种风格去做前后置的使用



全局共享文件conftest.py(可以理解为全局变量)
1、conftest.py要手动创建，并且名称不能改必须是conftest.py
2、使用的时候不需要导入的，自动识别的
3、使用的时候建议写上@pytest.mark.usefixtures('init_class')
4、必须创建在rootdir下面或者是子目录下面，pytest支持乡下递归查找到conftest.py
5、conftest.py文件支持多个的，但是不能在同一个目录下
6、一个项目写一个conftest.py

举例一：子目录可以向上共享conftest.py,就近原则
py52/day41/main.py conftest.py  在这里执行的时候 使用自己目录的conftest.py
py52/day42/main.py conftest.py  在这里执行的时候 使用自己目录的conftest.py
py52/day42/main.py  在这里执行的时候 使用兄弟目录(day41)的conftest.py,如果兄弟目录还没有就用父目录的

举例二：不能向下共享conftest.py
py52/day41/main.py  在这里执行的时候，使用不到conftest.py里面的东西
py52/day41/day42/main.py conftest.py 

总结：
1、conftest.py所在的目录子目录可以使用，和conftest.py是兄弟目录下的可以使用
2、conftest.py父目录不能使用
3、一个项目可以有多个conftest，但是不能放同一个目录下

=============================================

前置sql语句

@pytest.fixture(params=['1','2','3']，name='demo')
def init_login():
    print("前置")
   
@pytest.mark.usefixtures("init_login")
def test_01():
    pass
    
    
    
1、参数替换
2、执行前置sql语句
    
请求接口的前置条件：1,2 
@pytest.mark.usefixtures("1")
@pytest.mark.usefixtures("2")
def send_req():
    pass
    
    
    
"""


