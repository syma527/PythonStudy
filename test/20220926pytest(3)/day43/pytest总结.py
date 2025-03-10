"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/9/26 21:27
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、pytest和unittest区别
1、unittest是入门级别的
2、pytest是进阶的框架

二、用例编写
1、pytest与unittest编写规范差不多的，unittest支持pytest也支持(记住unittest的编写规范就行)

三、pytest前置后置
1、和unittest前后置一样的，写在测试用例类里面的【了解】
2、自定义前置后置,yield关键字来区分前后置
   @pytest.fixture(scope="class")
   前后置的用法：函数用例的用法，类里面的用法
3、pytest前置后置的级别设置
   conftest.py全局前后置文件，注意文件的优先级(一个项目写一个conftest.py，放到项目跟目录)
   scope="class"
   scope="function"
4、用例收集
   自动收集测试用例
   指定收集的测试用例文件或者是类
   根据pytest的标记收集测试用例

四、数据驱动
   @pytest.mark.parametrize("case",case_list)
   函数
   类

五、pytest的标签
   pytest.ini文件的写法
   怎么执行特定标签的测试用例
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
    
六、失败重运行
    失败重运行
    --reruns：设置重运行的次数
    --reruns-delay：重运行的间隔时间，秒为单位
    pytest.main(['-sv','demo01.py','--reruns','2','--reruns-delay','1'])

allure 单独的程序，目的就是展示测试报告
1、生成allure测试报告文件
2、allure有个自己的服务，启动这个服务，把allure测试报告文件解析，渲染出来
3、allure命令配环境变量(jenkins)、jdk的环境变量

"""