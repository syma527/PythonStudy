"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/7/18 20:12
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、文件操作(纯文本文件)
1、动态拼接路径
res = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(res,"a.txt")
print(file_path)

2、文件读取
file: 文件，需要传绝对路径，默认是当前目录
mode：操作模式，r：读取文件，w；写文件  a:追加写文件
encoding="utf-8": 编码格式，处理中文的，如果有中文读取会报错
file = open(file="a.txt",mode="r",encoding="utf-8")
result = file.read()
print(result)
file.close()


3、上下文管理协议
with语法,在使用完成之后会自动关闭文件IO
with open(file="a.txt",mode="r",encoding="utf-8") as file:
    result = file.read()
    print(result)

result = file.read() #全部读取
result = file.readline() #读取第一行，以回车或者是换行符为准
result = file.readlines() #读取所有的行，每一行作为列表的一个元素(会将换行符读取出来)，返回一个包含所有行的列表，
print(result)

4、写文件
with open(file="b.txt",mode="w",encoding="utf-8") as file:
    file.write("20220718")
1、覆盖写入(写一个值)
file.write("20220718")
2、写多个值
如果要换行需要自己添加换行符进来，否则会写到一行
file.writelines(["11\n","22","33"]) #一次性写多个
3、追加写入
在最后一行的末尾追加写入
如果要换行需要自己添加换行符进来，否则会写到一行
with open(file="b.txt",mode="a",encoding="utf-8") as file:
    file.writelines(["python","22","33"]) 


5、操作模式
with open(file="b.txt",mode="r+",encoding="utf-8") as file:
mode取值
1、只读文件：r
   1、文件必须要存在,不存在会报错
   2、默认是只读模式
   3、如果只是r模式，不能写文件
2、只写文件: w
   1、文件可以不存在，如果文件不存在会自动创建文件
   2、如果写文件不指定路径，会保存在当前目录下，如果指定了路径，这个路径一定要存在
   3、覆盖写入，会删掉之前的内容
   4、如果只是w模式，不能读取
3、追加写入文件:a
   1、追加写入，会在文件末尾写入(在文件所在的光标处开始写入)
   2、文件可以不存在，如果不存在会自动创建
   3、如果写文件不指定路径，会保存在当前目录下，如果指定了路径，这个路径一定要存在
4、+：追加另一种操作模式
   r+: 读+覆盖写
   w+：覆盖写+读
   a+: 追加写+读
5、图片或者视频读写
   wb：写(保存文件或者图片)
   rb：读
   ab: 追加写文件
   
6、光标处理(不要一边写一边读)
file.seek(0)
offset:偏移量
whence: 位置(从哪里开始偏移)  0：默认是0，是文件开头位置  1：当前光标位置  3：文件末尾
with open(file="v.txt",mode="w+",encoding="utf-8") as file:
    file.write("python123") # 覆盖写入，一次只能写一个值
    file.seek(0) #设置光标位置，这里是设置到文件开头的位置
    # offset:偏移量
    # whence: 位置(从哪里开始偏移)  0：默认是0，是文件开头位置  1：当前光标位置  3：文件末尾
    reslut = file.read()
    print("读取结果：",reslut)
"""
import os



with open(file="v.txt",mode="w+",encoding="utf-8") as file:
    file.write("python123") # 覆盖写入，一次只能写一个值
    file.seek(0) #设置光标位置，这里是设置到文件开头的位置
    # offset:偏移量
    # whence: 位置(从哪里开始偏移)  0：默认是0，是文件开头位置  1：当前光标位置  3：文件末尾
    reslut = file.read()
    print("读取结果：",reslut)








"""
with open(file="b.txt",mode="a",encoding="utf-8") as file:
    # file.write("python123") # 覆盖写入，一次只能写一个值
    file.writelines(["python","22","33"]) #一次性写多个


encoding
file = open(file="a.txt",mode="r",encoding="utf-8")
result = file.read()
print(result)
file.close()



with open(file="b.txt",mode="r",encoding="utf-8") as file:
    # result = file.read() #全部读取
    # result = file.readline() #读取第一行，以回车或者是换行符为准
    result = file.readlines() #读取所有的行，每一行作为列表的一个元素(会将换行符读取出来)，返回一个包含所有行的列表，
    print(result)

"""


