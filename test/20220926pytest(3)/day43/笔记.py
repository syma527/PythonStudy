"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/9/26 20:54
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、pytest.ini
语法模板：
[pytest]
markers=
    login:python52_pytest
    py56:python56_pytest
规则：
1、pytest.ini文件名必须是这样写，不能随便写
2、markers=必须这么写不能改
3、不能写注释，不支持写注释


二、打标签
1、给用例打标签
作用域：标签只对打个测试用例起作用
@pytest.mark.login
def test_02():
    print("test_02")
2、给用例打多个标签
@pytest.mark.login
@pytest.mark.py56
def test_02():
    print("test_02")

3、给类(里面的测试用例)打标签
作用域：整个测试用例类里面所有的测试用例
@pytest.mark.login
class TestDemo:
    def test_03(self):
        print("test_03")
    def test_04(self):
        print("test_04")
        
4、给类(里面的测试用例)打多个标签
作用域：整个测试用例类里面所有的测试用例
@pytest.mark.login
@pytest.mark.py56
class TestDemo:
    def test_03(self):
        print("test_03")
    def test_04(self):
        print("test_04")
        
5、给类(里面的测试用例)打标签，通过全局变量来实现      
   pytestmark这个类属性名称不能改
   支持打多个标签
   作用域：整个测试用例类里面所有的测试用例
class TestDemo:
    pytestmark=[pytest.mark.login,pytest.mark.py56]

    def test_03(self):
        print("test_03")

    def test_04(self):
        print("test_04")


三、根据标签执行对应标签的测试用例
1、单独收集标记的测试用例，不要在测试用例文件去自动收集执行
pytest.main(['-sv','demo02.py','-m=py56'])

逻辑运算 or、and、not
2、执行多个标签的用例,or是或者的意思，只要用一个标签都会执行
pytest.main(['-sv','demo03.py','-m=py56 or login'])

3、执行多个标签的用例,and 是和的意思，两个标签都要有才会执行
pytest.main(['-sv','demo03.py','-m=py56 and login'])

4、不执行某个标签的测试用例,只要打了某个不执行的标签，就不会被执行
pytest.main(['-sv','demo03.py','-m=not py56'])

5、通过文件名称和类名称用例名称来指定执行某些测试用例
#执行指定文件的测试用例，或者是测试用例类
pytest.main(['-sv','demo03.py::test_11'])


四、失败重运行
失败重运行
--reruns：设置重运行的次数
--reruns-delay：重运行的间隔时间，秒为单位
pytest.main(['-sv','demo01.py','--reruns','2','--reruns-delay','1'])



"""