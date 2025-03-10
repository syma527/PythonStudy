"""
============================
Project: py52Api
Author:柠檬班-海励
Time:2022/8/26 20:06
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
一、参数替换的思路
为什么要替换参数：请求参数不一定都是写死的数据，有可能存在接口数据依赖
1、在excel参数中写入特殊标记(#key#)，说明写了特殊标记的地方需要被替换
2、读取excel中的参数，通过正则表达式提取需要替换的key，得到一个list
3、遍历list，根据list中不同的参数，去不同的地方获取对应的数据(脚本生成的数据、配置文件来源数据、默认从全局变量获取数据)
4、获取到需要替换数据的value，设置为全局变量(通过类属性来实现)
5、遍历list，通过字符串的replace方法进行数据替换
6、替换完成之后将替换后的数据转换成python对象

二、响应结果处理思路
为什么要处理响应结果：接口返回数据类型不一致，我们后续需要去响应结果中提取参数，解决参数依赖问题(jsonpath提取器)
1、我们需要的是json数据，对于所有的返回数据我们进行二次封装，封装成固定的格式
2、传入响应数据对象，通过json方式去获取对应的body内容，如果不是json数据那就说明不是我们需要的类型，就会报错，此时我们进行二次封装处理
   符合要求的数据，直接进行二次封装处理

三、接口断言的思路
1、在excel中新增一个字段expected_data
2、expected_data字段存放期望结果{"token_type":"bearer"}，可以写多个key-value,期望结果数据是单独请求接口或者查看接口文档获取到的
3、获取期望结果数据，转换成dict类型，再遍历字典的key，然后去接口响应结果中通过key获取对应的value，组成新的字典，这个新的字典就是实际结果
4、通过TestCase类的断言去对期望结果和实际结果进行比对(直接比对字典)
5、因为字典数据只要key和value是一样的，不管位置是否一致，都认为是相等的

四、提取全局变量的思路
1、在excel中新增字段extract_data
2、extract_data字段放入数据{"access_token":"$..access_token"}
3、key表示要去响应结果中提取的key，value是提取key的jsonpath表达式
4、获取extract_data数据，转换成dict类型，再遍历字典的key和value，通过key和value(jsonpath表达式)去响应结果中提取对应key的数据
5、提取数据出赖之后，通过类属性设置为全局变量(属性的key就是刚才遍历的key，属性的值为通过jsonpath表达式提取出来的数据)

五、鉴权的思路
为什么要鉴权：一些接口需要登陆之后才能请求的接口(相当于是接口的前置条件)
1、将接口的前置条件放到该接口之前执行，执行后通过提取token的方式再设置到请求头完成鉴权
2、提取登陆接口中的token数据，设置为类属性(全局变量)
3、在请求所有的接口之前，判断一下类属性是否有token属性，如果有就将token按要求设置到请求中
4、后面的接口请求的时候统一带上有鉴权信息的请求头

六、发送请求封装的思路
1、发送请求之前去调用鉴权处理的方法，获取最新的请求头数据
2、在excel中新增is_upload字段，如果字段为1表示是图片上传几口，否则为普通接口
3、判断该接口是否是图片上传接口，如果是图片上传接口就调对应的图片上传方法，如果不是就走else的逻辑发送普通请求
4、在请求图片上传接口的时候，要对应修改请求字段Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryfiTjkFx67gFh7If
5、为了跨平台，放到jenkins上做持续接触，将需要上传的图片放到项目images目录下(放哪里都可以合理就行)
6、图片上传接口请求完成之后，要讲请求头修改为json格式，否则后面非图片上传的接口就会报错

七、数据库的断言思路
1、把图片上传的返回的数据提取出来，设置为全局变量
2、拿到全局变量去数据库去查询(连数据库+拼接sql语句)
3、在excel新增assert_db字段存放数据库断言的期望结果和实际结果获取需要执行的sql语句
4、先判断是否需要替换sql中的数据，如果要替换，先替换sql语句再执行sql语句，再断言

八、sql语句替换的思路
1、连数据库
2、替换sql
3、执行sql




expected_data = {"token_type":"bearer"}
actual_data =  {"token_type":"bearer"}

{"expected_data":1,"actual_data":"select count(*) from tz_attach_file where file_path = '#file_path#'"}
select count(*) from tz_attach_file where file_path = "2022/08/e56db2815a694b0180c4f520efdd9759.png";
"""



