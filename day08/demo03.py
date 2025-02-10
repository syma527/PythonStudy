"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/4 21:20
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
函数
一、什么是函数
1、一段可以被别人(其他程序)调用的代码或者是程序

2、语法
def add():
    num = 1 + 2
    print(num)
    return num

3、注意点：
   1、函数命名规则，下划线连接方法，见文知意
   2、函数里面的代码体要缩进，TAB == 4个空格
   3、函数的返回值，遇到return语句表示函数运行结束，return可以写可以不写
   4、return后面可以写具体的值，也可以写变量或者对象，如果return后面什么都不写默认返回None
   5、函数如果不调用不会执行的

4、函数调用
   1、函数名(参数)
   2、类实例.函数名称(参数) #类和对象讲


二、函数的参数
1、形参：占个位置，具体这个位置是谁不一定，谁调用谁传
2、实参：函数调用的时候，实际传进来的参数

参数分类
必须参数: 函数定义的时候，如果需要调用者必须传递参数进来，就用必须参数
1、语法
def add(x,y):
    print("x的值",x)
    print("y的值",y)
    return x+y
2、注意点：
   1、必须参数在调用的时候必须要传递，不传会报错
   2、必须参数按顺序传入的，定义的时候在前面，传参就要传到前面才能被对应的参数接收

关键字参数: 在调用函数的时候，传参方式以key = value 的方式传递参数
1、语法：result = add(y=3,x=5)
2、注意点：
   1、传参的时候一定要用Key=value的方式


默认参数：默认参数就是在定义的时候给必须参数写了个默认值
1、调用的时候默认参数可以不传参
2、如果默认参数不传参，就使用默认的值，如果传参了就使用传参的值
def add(x=1,y=1):
    print("x的值",x)
    print("y的值",y)
    return x+y

不定长参数
*args: 接收必须参数，接收的值会放到元组中
**kwargs: 接收关键字参数，接收的值会放到字典里面
*args 和 **kwargs 必须放在必须参数后面
先满足必须参数的取值，再给不定长参数
在函数内部使用的时候 不要加 *号
def sum_num(name,age,*args,**kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)

sum_num("老王",30,90,89,first_name="法外狂徒张三")

三、解包
字典解包
test_dict = {"name":"张三","age":"20"}
result = add(**test_dict) # add(name="张三",age="20") 关键字参数传参
print(result)

列表解包
test_list = [2,3]
res = add(*test_list)  # add(2,3) 必须参数传参
print(res)
"""
def add(**kwargs):
    return kwargs
test_dict = {"name":"张三","age":"20"}
result = add(**test_dict) # add(name="张三",age="20") 关键字参数传参
print(result)

# test_list = [2,3]
# # res = add(test_list[0],test_list[1])
# res = add(*test_list)  # add(2,3) 必须参数传参
# print(res)





"""

def sum_num(name,age,*args,**kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)

sum_num("老王",30,90,89,first_name="法外狂徒张三")



def add(x=1,y=1):
    print("x的值",x)
    print("y的值",y)
    return x+y
result = add(x=6,y=4)
print(result)


def add(x,y):
    print("x的值",x)
    print("y的值",y)
    return x+y

result = add(y=3,x=5)
print(result)


def add():
    num = 1 + 2
    print(num)
    #return num

# result = add()
# print(result) # None

# add()
"""